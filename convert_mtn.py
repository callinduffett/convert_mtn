import os
import csv
import sys
os.chdir(r"directory goes here")
txt_file = r"sample.txt"
csv_file = r"sample.csv"

#headers = ["time", "surge", "sway", "heave", "roll", "pitch", "yaw"]
in_txt = csv.reader(open(txt_file, "rt"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wt'))
out_csv.writerows(in_txt)

with open(csv_file, 'w') as out_csv_head:
    writer = csv.DictWriter(out_csv_head, fieldnames=["time", "surge", "sway", "heave", "roll", "pitch", "yaw"], delimiter=',')
    writer.writeheader()

