import sys
import os


from src.csvToJson import  convertCsvTojson
from src.prettyPrint import prettyPrint

from src.matchesPerSeason1 import matchesPerSeason
from src.matchesWonPerTeamPerYear import matchesWonPerTeamPerYear
from src.extraRunsConcededPerTeamInYear2016  import extraRunsConcededPerTeamInYear2016
from src.top10EconomicalBowlersIn2015 import top10EconomicalBowlersIn2015
from src.teamWonTossAndMatches import teamWonTossAndMatches

import csv
import json

matches = convertCsvTojson('data/matches.csv')  
deliveries = convertCsvTojson('data/deliveries.csv')  

# 1st question 
prettyPrint(matchesPerSeason(matches))
# 2nd question 
prettyPrint(matchesWonPerTeamPerYear(matches))
# 3rd question
prettyPrint(extraRunsConcededPerTeamInYear2016(matches, deliveries))
# 4th question
prettyPrint(top10EconomicalBowlersIn2015(matches, deliveries))
#5th question
prettyPrint(teamWonTossAndMatches(matches))
