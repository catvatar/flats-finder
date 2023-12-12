# flats-finder
## General info
This is a python code to find and retreive the most important data about flats from Otodom website.

## Dependencies
To run this project, you will have to clone this repository and then create and activate a conda environment:
```
$ conda create -n flats
```
```
$ conda activate flats
```
```
pip install openpyxl selenium==4.9.0
```
Also, download geckodriver from `https://github.com/mozilla/geckodriver/releases` and put it in the directory with source code.

## Variables
If you want to personalize your search, modify undermentioned variables in main.py:
* price_min
* price_max
* min_area
* max_area

## Run
To run the script just do
```
$ python3 main.py
```