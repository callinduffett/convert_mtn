import os
import csv
import os.path

mtn_path = (r"DIRECTORY")
os.chdir(str(mtn_path))

mtn_list_file = "Extoutput.csv"
with open(mtn_list_file, 'r') as f:
