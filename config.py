import datetime as dt
import urllib.parse

import json

# Parameters for requests
distance = "800"  # e.g. (50, 100, 200, 400, 800, 1500) Change as appropriate
gender = "M"  # e.g. (M or F or X [for mixed events]) Change as appropriate
stroke = "FREESTYLE"  # e.g. (BREASTSTROKE, MEDLEY, MEDLEY_RELAY, FREESTYLE, FREESTYLE_RELAY) Change as appropriate
poolConfiguration = "LCM"
year = ""  # year leave blank if filtering by date
startDate = "01%2F07%2F2024" #startDate is URL encoded. For example if 1st of January 2019, this will be 01%2F01%2F2019
#endDate = urllib.parse.quote(dt.datetime.today().strftime("%d/%m/%Y"), safe='') #endDate is URL encoded. By default, it is set to today's date.
endDate = "11%2F08%2F2024"
timesMode = "ALL_TIMES"
pageSize = "200"
countryId = ""

# Load the countries.json file
with open('countries.json', 'r') as file:
    countries_data = json.load(file)

# Extract all country names
countries_list = [country['Name'] for country in countries_data]

# Define Countries to get results from
"""
countries_list = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "Bahrain",
    "Brunei Darussalam",
    "Cambodia",
    "Democratic People's Republic of Korea",
    "Democratic Republic of Timor - Leste",
    "Hong Kong, China",
    "Indonesia",
    "India",
    "Islamic Republic of Iran",
    "Iraq",
    "Jordan",
    "Japan",
    "Kazakhstan",
    "Kyrgyzstan",
    "People's Republic of China",
    "Republic of Korea",
    "Saudi Arabia",
    "Kuwait",
    "Lao People's Democratic Republic",
    "Lebanon",
    "Macau, China",
    "Malaysia",
    "Maldives",
    "Mongolia",
    "Myanmar",
    "Nepal",
    "Oman",
    "Pakistan",
    "Philippines",
    "Palestine",
    "Qatar",
    "Singapore",
    "Sri Lanka",
    "Syrian Arab Republic",
    "Thailand",
    "Tajikistan",
    "Turkmenistan",
    "Chinese Taipei",
    "United Arab Emirates",
    "Uzbekistan",
    "Vietnam",
    "Yemen"

    """