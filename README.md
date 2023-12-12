# flats-finder
## General info
This is a python code to find and retreive the most important data about flats from Otodom - polish housing website. The data is presented in .xlsx file.

## Dependencies
To run this project, you will have to clone this repository, create and activate a conda environment with openpyxl and selenium:
```
conda create -n flats python=3.12
conda install -n flats pip
conda activate flats
pip install openpyxl selenium==4.9.0
```
Also, download geckodriver from `https://github.com/mozilla/geckodriver/releases` and put it in the directory with source code.

## Variables
If you want to personalize your search, adjust undermentioned variables:
```
options:
  -h, --help            show this help message and exit
  --price_min PRICE_MIN
                        Set minimum price
  --price_max PRICE_MAX
                        Set maximum price
  --min_area MIN_AREA   Set minimal area of flat
  --max_area MAX_AREA   Set maximal area of flat
  --place PLACE         Set location of flat
  --time_filter {any,last24h,last3d,last7d}
                        Set filtering for time of adding offer to Otodom
```

## Run
To run the script with default values just do
```
python3 main.py
```