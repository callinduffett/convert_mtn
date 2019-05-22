import os
import csv
import os.path
mtn_path = r"DIRECTORY"
a = open(mtn_path + "output.csv", 'r+')
num_files = 0
for path, dirnames, filenames in os.walk(mtn_path):
    for filename in [f for f in filenames if f.endswith(".txt")]:
        f = os.path.join(path, filename)
        a.write(str(f) + os.linesep)
        num_files = num_files + 1
#
print("The total number of text files found was " + str(num_files))