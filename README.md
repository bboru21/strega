# Strega
Script for scraping the Virginia ABC stores website, and getting the best deals.

## Initial Setup
Run the bash script which will create the VirtualEnvironment and install Python packages:
`sh setup.sh`

## Usage
Activate virtual environment: `source virtualenv/bin/activate`

## Create Database Tables
`python create_database.py  --settings=settings_local`

## Get Monthly Cocktails
`python get_cocktails.py  --settings=settings_local`

## Get ABC Prices
Run script: `python strega.py  --settings=settings_base`

## User Agents
The script uses random browser user agent strings that are listed in the settings file. You may wish to update this list from time to time with more modern agents.
