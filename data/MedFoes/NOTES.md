This folder contains the setup and partial (collated) output for the long-duration MedFoes runs.

All of the data used for analysis is contained in the `runsets/<CALLSIGN>_collated_data_out.npz` files.
The raw output files are available upon request, but are many million individual files
and consume a large amount of space.

The actual runs were done on an HPC with Sun Grid Engine (SGE) using
the `runsets/<CALLSIGN>/mfp_longrun_array.sge` script files.

The binary (Java JAR file) used to generate the data here is `MedFoesP-0.6.2.jar`.  
The source is in the `code` directory of this supplemental as `medfoes-0.6-0.6.2.tar.gz` 
as well as available on GitHub: https://github.com/travc/medfoes-0.6/releases/tag/v0.6.2

NOTE: Some of the MedFoes output files incorrectly say "days" when they should say "hours".

## Running MedFoes runsets

For a particualr station where we have already generated the temperature dataset,
for example: KLAX with temperature file `temperatures/KLAX_AT_cleaned_trimmed.csv`.  
CALLSIGN is the weather station callsign, eg: KLAX, KMIA, ect.

* `cd runsets`
* `./setup_runs.sh <CALLSIGN>`  
  This assumes temperature file is at `../../temperatures/<CALLSIGN>_AT_cleaned_trimmed.csv`
* `cd ..`
* `./do_medfoes_runs.sh runsets/<CALLSIGN>`
* use qstat and check the output files to make sure it is going correctly
* wait until they have finished
* `cd runsets`
* `../collate_longrun_output.py <CALLSIGN>`
* The `<CALLSIGN>_collated_data_out.npz` file is now ready for analysis

