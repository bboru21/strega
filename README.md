# Strega
Script for scraping the Virginia ABC stores website, and getting the best deals.

## Initial Setup
Run the bash script which will create the VirtualEnvironment and install Python packages:
`sh setup.sh`

## Download Chrome Driver
Download ChromeDriver the following URL, and make sure to un-zip it within the directory where you've cloned this script: https://sites.google.com/a/chromium.org/chromedriver/

Selenium Python Documentation can be found here: https://selenium-python.readthedocs.io/api.html

## Usage
Activate virtual environment: `source virtualenv/bin/activate`

## Create Database Tables
`python create_database.py  --settings=settings_local`

## Get Monthly Cocktails
`python get_cocktails.py  --settings=settings_local`

## Get ABC Prices
Run script: `python get_abc_prices.py  --settings=settings_local`

## User Agents
The script uses random browser user agent strings that are listed in the settings file. You may wish to update this list from time to time with more modern agents.
