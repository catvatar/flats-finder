# flats-finder
## General info
This is a python code to find and retreive the most important data about flats from Otodom - Polish housing website.

## CLI
To run as CLI version, use `conda`:
```
conda create -n flats python=3.12
conda install -n flats pip
conda activate flats
pip install openpyxl selenium==4.9.0
```

You may need to install `geckodriver` separately.

Run with:
```
python3 API/src/scraper/main.py
```

Use the following CLI parameters to customize your search:
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
  --market_type {any,primary,secondary}
                        Set market type of flat
```

## Web version
To run this project as a web app you will need `docker`.

Run this inside main directory of this repo:
```
docker build -t flat-finder-api API
docker run -d -p 8000:8000 flat-finder-api
```

### Development
For development, run with:
```
docker run -d --name flat-finder-api -p 8000:8000 -v $(pwd)/API/src:/src flat-finder-api
```

## API
The same parameters are available for use with API as with CLI.

Example request:
```
curl 'http://127.0.0.1:8000/?price_min=0&price_max=600000&min_area=35&max_area=100&place=Ursus&time_filter=last3d&market_type=any'
```

## Web client
Coming soon.