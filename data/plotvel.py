#plotvel.py
#reads .kel file that is located in same directory as this program
#converts velocity from m/s into km/s
#plots intensity vs velocity

#enter lower and upper bounds below
lowerbound=-200*1000
upperbound=+200*1000

import os
import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#Initialize variables
GALLON=[0];GALLAT=[0];velocity=[0];intensity=[0];correction=0;colon=[999]

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
            if vel>=lowerbound and vel<=upperbound:
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
            x=(float(linestring[1]))/1000.0
            velocity.append(x)
            y=float(linestring[2])
            intensity.append(y)
f.closed
True
GALLON.pop(0);GALLAT.pop(0);velocity.pop(0);intensity.pop(0)

#plot intensity vs velocity
fig=plt.figure(figsize=(10,6))
ax=plt.axes()
ax.set_title("Intensity vs Velocity",fontsize=20)
ax.set_xlabel("Velocity (km/s)", fontsize=18)
ax.set_ylabel("Intensity (Kelvins)", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
#ax.set_xticks([-200,-150,-100,-50,0,50,100,150,200])
ax.scatter(velocity,intensity, c="red",s=60,label=("GLONG,GLAT= "+str(int(GALLON[0]))+"  "+str(int(GALLAT[0]))))
ax.legend(loc="best")
plt.show()

exit()
