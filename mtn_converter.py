# this script should open a csv file that contains a list of .txt files in a directory,
# then add a header row and convert the file to a csv and save it in the same folder
import os
import csv
import os.path

mtn_path = (r"DIRECTORY")
os.chdir(str(mtn_path))

mtn_list_file = "Extoutput.csv"
with open(mtn_list_file, 'r') as f:
