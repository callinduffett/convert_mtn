import os
import csv
import sys
os.chdir(r"G:\US-Houston\Projects\110183 SHELL VITO CVA\Powernap CVA\TimeHistory\Ext\tdb\INT_NR_H10Cu\000\002")
txt_file = r"sample.txt"
csv_file = r"sample.csv"

#headers = ["time", "surge", "sway", "heave", "roll", "pitch", "yaw"]
# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
in_txt = csv.reader(open(txt_file, "rt"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'wt'))
out_csv.writerows(in_txt)

with open(csv_file, 'w') as out_csv_head:
    writer = csv.DictWriter(out_csv_head, fieldnames=["time", "surge", "sway", "heave", "roll", "pitch", "yaw"], delimiter=',')
    writer.writeheader()

