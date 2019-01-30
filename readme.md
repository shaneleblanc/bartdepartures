# BART Departure Times CLI Tool
### Description
Uses the public BART API to pull station information and check for trains leaving from the station chosen. Compatible with Python 3.*, Python 2 works but will output less presentable strings.
### Instructions 
- Execute with `python3 bdep.py` to see a list of stations. Enter the number of the station from the list of stations that you would like to see departure times for. 
- Execute with `python3 bdep.py [STATION ABBREVIATION]` to skip listing stations and output departure times for a specific station. 
- Execute `python3 bdep.py list` to see a list of stations and their abbreviations
### Note about API key
The BART API key used here is the No strings attached, public key available at <https://www.bart.gov/schedules/developers/api>. This key is subject to change. 