import sys
import os


from src.csvToJson import  convertCsvTojson
from src.MatchesPerSeason1 import matchesPerSeason

import csv
import json

matches = convertCsvTojson('data/matches.csv')    

# 1 question 
print(matchesPerSeason(matches))
# 2 question 
