import sys
import json
import pandas as pd

csv_file = None
if len(sys.argv) < 2:
    print ("Usage: python csv2json.py 313024294.csv")
    print("Default csv filename: 313024294.csv")
    csv_file = "313024294.csv"

if csv_file is None:
    csv_file = sys.argv[1]
print()
print("Reading CSV file")
data = pd.read_csv(csv_file, 
    header=None, 
    encoding='latin-1', # decoding using lower encoding type 'latin-1' istead of utf-8 because the given input file has not been saved in utf-8 format
    engine='python') 

# removing empty columns
print("Removing empty columns")
data = data.dropna(how='all', axis='columns')

# converting to json
print("Converting to json")
json_output_file = csv_file[:-4] + '.json'
result = data.to_json(json_output_file, orient="values", indent=2)
# output json object format: 
# for orient="index" in above line
#  {
#      "index_id":{
#           "column_id": "data"
#           "column_id": "data"
#           ...
#      }
#  }
# for orient = "values"
# [
#      [
#           "data1",
#           "data2"
#           ...
#      ]
#  ]

print("Output json filename: ",json_output_file)
