# paper-Predicted-MF-Quarantine-Length-Data-and-Code
Data and code for the paper "Evaluation of predicted Medfly (Ceratitis capitata) quarantine length in the United States utilizing degree-day and agent-based models" by Travis C. Collier and Nicholas C. Manoukis

### General Notes

`.h5` files are hdf5 format files readable by the Python Pandas module or other standard tools.


### Filemap

* [README.md](./README.md) : This file
* [code/](./code) : Scripts and programs
   * [Batch fetch and process temperatures.ipynb](./code/Batch%20fetch%20and%20process%20temperatures.ipynb) : 
   Batch runs `Fetching and parsing ISH.ipynb` and `Cleaning temperatures.ipynb` for all sites
   * [Fetching and parsing ISH.ipynb](./code/Fetching%20and%20parsing%20ISH.ipynb) : 
   Download and initial processing of weather staion (site) temperature data
   * [Cleaning temperatures.ipynb](./code/Cleaning%20temperatures.ipynb) :
   Resampling, outlier removal, and gap filling of temperature data
   * [**Summary Figures.ipynb**](./code/Summary%20Figures.ipynb) : 
   **Generate figures and perfom statisical analysis**
   * [Temperature functions.ipynb](./code/Temperature%20functions.ipynb) : 
   Utility funcitons for operating on temperature data, **includes degree day calculation methods**
   * [Temperature datasets summary.ipynb](./code/Temperature%20datasets%20summary.ipynb) :
   Parse weather station (site) metadata and output `stations_summary.csv` used to generate sitemap figure
   * [stations_summary.csv](./code/stations_summary.csv) : Intermediate output; summary of stations metadata
   * [medfoes-0.6-0.6.2.tar.gz](./code/medfoes-0.6-0.6.2.tar.gz) :
   Full source of MED-FOES Agent-Based Simulation used 
* [data/](./data) : Input data and results; includes raw and cleaned teperature data
   * [APHIS CA quarantines.csv](./data/APHIS%20CA%20quarantines.csv) : Historic California Medfly quarantines
   * [MedFoes/](./data/MedFoes) : MED-FOES runsets; includes compiled program (jar file) and helper scripts
     * *See contained `NOTES.md` file*
 * [temperatures/](./data/temperatures) : Raw and cleaned temperature data
   * *See `Fetching and parsing ISH.ipynb` and `Cleaning temperatures.ipynb` which generated these files*
   * [ISD/](./data/temperatures/ISD) : Original atmospheric temperature values extracted from NOAA ISD dataset by `Fetching and parsing ISH.ipynb`
   * *For Each station (site) there are the following files*
     * `ISD/{STATION}_AT.h5` : All the NOAA ISD atmospheric temperature data for STATION merged together
     * `{STATION}_AT_cleaned.h5` : Outliers removed, resampled to hourly on the hour, and gaps filled. **Used for of degree day calculations and MED-FOES runsets**
     * `{STATION}_AT_cleaned_trimmed.csv` : Converted to `csv` format and trimmed to start date for MED-FOES input
     * `{STATION}_AT_gaps.tsv` : List of large (>3hr) gaps which required filling by day over day interpolation
     * `{STATION}_outlier.png` : Figure showing outliers removed
     * `{STATION}_cleaning.png` : Figure comparing raw vs cleaned temperature data
 * [figs](./figs) : Destination directory for `Summary Figures.ipynb`
   * [NOTES.md](./figs/NOTES.md)
- [LICENSE](./LICENSE)
