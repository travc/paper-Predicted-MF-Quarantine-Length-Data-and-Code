#!/bin/bash

STATION=$1
TFILE="../../../temperatures/${STATION}_AT_cleaned_trimmed.csv"
SKEL_DIR='skel'

tfile_link="temperature_file.csv"

echo $STATION $TFILE

#mkdir "$STATION"
#cp -v "$SKEL_DIR/mfp.cfg" "$STATION"
#cp -v "$SKEL_DIR/mfp_longrun_array.sge" "$STATION"

cd $STATION
ln -s "$TFILE" "$tfile_link"
cd ..
