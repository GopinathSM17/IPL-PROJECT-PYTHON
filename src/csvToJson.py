import csv
import json

def convertCsvTojson(filePath):
    with open(filePath, mode='r', encoding='utf-8') as file :
        data = list(csv.DictReader(file))
    return data

