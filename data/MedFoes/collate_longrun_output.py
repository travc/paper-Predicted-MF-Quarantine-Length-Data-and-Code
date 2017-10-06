#!/bin/env python3

import sys
import os
import glob

import numpy as np
import pandas as pd

from collections import OrderedDict

RUNSET = sys.argv[1].rstrip('/')


BASEDIR = './'
OUTDIR = 'out'

INTERPOLATION_METHOD = 'nearest'

STEP_FILENAME_GLOB = 'step_*'
MEDFOESP_DETAIL_FILE_GLOB = 'MED-FOESp_*_detail.txt'
DATA_OUT_FILENAME = RUNSET+'_collated_data_out.npz'


TFILE = os.path.join(BASEDIR, RUNSET, 'temperature_file.csv')
STEP_SIZE = 24*7  # Each step is one week
RUNS_PER_STEP = 2500

# read in the temperature file
tempdf = pd.read_csv(TFILE, index_col='datetime', parse_dates=True)
print("Read temperature file '{}'".format(TFILE))

# Get list of all the run directories
rootpath = os.path.join(BASEDIR, RUNSET, OUTDIR)
dirs = sorted([os.path.split(x)[1] for x in glob.glob(os.path.join(rootpath, STEP_FILENAME_GLOB))])
#print(rootpath)
#print(dirs)

# ensure step numbers make sense (consecutive starting from 1)
tmp = min(dirs).split('_')[1]
assert int(tmp) == 1, "ERROR?: First step number should be 1, right?"
num_steps = int(max(dirs).split('_')[1])
assert num_steps == len(dirs), "ERROR?: Last step number should be the number of steps... ie. no missing steps."

# determine the start datetime for each step
stepdir2startdate = {}
tempfile_startdt = tempdf.index[0]
task_nums = [int(x.split('_')[1]) for x in dirs]
date2step = pd.DataFrame(index=[tempfile_startdt+pd.Timedelta(hours=STEP_SIZE*(x-1)) for x in task_nums],
                         data=list(zip(task_nums, dirs)),
                         columns=['step_num','step_dir']).sort_index()

max_run_length = 0
prop_extinct = OrderedDict() # key is runset start datetime (value)
start_times = []

# For each step, read the medfoesp detail file
for start_time, row in date2step.iterrows():
    step_dir = row['step_dir']
    print(start_time, step_dir)

    # find the medfoesp detail file for this step
    mfpdetail_fn = glob.glob(os.path.join(BASEDIR,RUNSET,OUTDIR,step_dir,MEDFOESP_DETAIL_FILE_GLOB))
    assert len(mfpdetail_fn) == 1, "Error: didn't find, or found more than one, MEDFOESP 'detial' file: {}".format(mfpdetail_fn)
    mfpdetail_fn = mfpdetail_fn[0]
    # read it
    tmp = pd.read_csv(mfpdetail_fn, sep='\t')
    # add an extirpation time column
    tmp['ext_time'] = tmp['run_time']
    tmp.loc[tmp['end_condition']!=0, 'ext_time'] = np.nan

    # This is a space (and time) efficient way of computing the proportion of runs going extinct
    # in the most accurate way possible...  But it is overkill here
    ext_cnts = tmp['ext_time'].dropna().value_counts(sort=False).sort_index()
    if len(ext_cnts) == 0:
        print("NO RUNS GOING TO EXTRIPATION FOR STEP "+step_dir)
        break
    cumcnt = np.cumsum(ext_cnts.values).astype(float)
    #prop_extinct[run_start_datetime]
    foo = np.array(list(zip(ext_cnts.index, cumcnt/cumcnt[-1])))

    start_times.append(start_time)
    prop_extinct[start_time] = foo

    run_length_max = ext_cnts.index.max()
    if max_run_length < run_length_max:
        max_run_length = run_length_max


np.savez_compressed(DATA_OUT_FILENAME,
                    runset_name=os.path.join(BASEDIR, RUNSET),
                    max_run_length=max_run_length,
                    prop_extinct=prop_extinct,
                    step2startdate=stepdir2startdate,
                    )
print("Data saved to: '{}'".format(DATA_OUT_FILENAME))
