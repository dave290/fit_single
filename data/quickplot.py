#quickplot.py
#plots single scan from a kel file
#file should be in the same directory as this program
#copy this program into the folder that contains the kel file
#to plot velocity, enter bounds in km/s
#python quickplot.py (-L -200 -H +200) optional
#to plot frequency, enter bounds in kHz
#python quickplot.py (-L 1419200 -H 1421600) optional

'''
import argparse
parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("-L", "--lower_bound", help="Enter lower bound in km/s or kHz", type=int)
parser.add_argument("-H", "--higher_bound", help="Enter higher bound in km/s or kHz", type=int)
args = parser.parse_args()
lowerfitthreshold=args.lower_bound*1000
upperfitthreshold=args.higher_bound*1000
'''
lowerfitthreshold=-200000
upperfitthreshold=+200000

import os
import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure(figsize=(12,6))

ax=plt.axes()
ax.set_title("Intensity vs Velocity")
ax.set_xlabel("Velocity (m/s)")
ax.set_ylabel("Intensity (K)")

#Initialize variables
GALLON=[0];GALLAT=[0];velocity=[0];intensity=[0]
colon=[999];correction=0

#Read the list of items in the working directory and find single file with .kel extension
dir_items=os.listdir()
number_of_items=len(dir_items)
for i in range(number_of_items):
    temp=dir_items[i]
    if temp[-4:]==".kel":
        datafile=temp

#determine start and end lines for reading data
with open(datafile, 'r') as f:  
    linesofdata=[0]
    line_no=0
    for line in f:
        line_no=line_no+1
        linestring=line.split()
        if linestring[0]=="#":
            pass
        else:
            vel=float(linestring[1])
            if vel>=lowerfitthreshold and vel<=upperfitthreshold:
                linesofdata.append(line_no)
        continue
f.closed
True
startline=int(linesofdata[1])
endline=int(linesofdata[-1])

#read file info
GALLON=[0];GALLAT=[0];velocity=[0];intensity=[0]
with open(datafile,'r') as f:
    N=0
    for line in f:
        N=N+1
        linestring=line.split()
        if linestring[1]=="GALLON":
            coordinate=linestring[3]
            for j in range(8):
                if coordinate[j]==":":
                    colon.append(j)
            degrees=float(coordinate[0:colon[1]])
            minutes=float(coordinate[colon[1]+1:colon[2]])
            seconds=float(coordinate[colon[2]+1:])
            degrees=degrees+minutes/60.0+seconds/3600.0
            gallon=float(round(degrees,2))
            colon=[999]
        if linestring[1]=="GALLAT":
            coordinate=linestring[3]
            if coordinate[0]=="-":
                multiplier=-1.0
            if coordinate[0]=="+":
                multiplier=+1.0
            for j in range(8):
                if coordinate[j]==":":
                    colon.append(j)
            degrees=float(coordinate[1:colon[1]])
            minutes=float(coordinate[colon[1]+1:colon[2]])
            seconds=float(coordinate[colon[2]+1:])
            degrees=multiplier*(degrees+minutes/60.0+seconds/3600.0)
            gallat=float(round(degrees,2))
            colon=[999]
        if N>=startline and N<=endline:
            GALLON.append(gallon)
            GALLAT.append(gallat)
            linestring=line.split()      
            x=float(linestring[1])
            velocity.append(x)
            y=float(linestring[2])
            intensity.append(y)
f.closed
True
GALLON[0]=GALLON[1];GALLAT[0]=GALLAT[1]
velocity[0]=velocity[1];intensity[0]=intensity[1]
ax.scatter(velocity,intensity,marker=".",label=("GLONG,GLAT= "+str(GALLON[0])+"  "+str(GALLAT[0])))
ax.legend(loc="best")

plt.show()
exit()
