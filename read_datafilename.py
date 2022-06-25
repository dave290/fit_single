#read_datafilename.py

import os

def get_datafilename():
    os.chdir('data')
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="File":  
                    filename=linestring[1]
                if linestring[0]=="Coordinate":
                    coordinate=linestring[1]
        f.closed
        True
    os.chdir("..")
    return filename,coordinate