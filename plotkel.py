#plotkel.py
#plots a single data scan from a .kel file
#this is not called by the fit programs, but is meant to be run independently
#August 7, 2022

import os
import read_parameters
import read_datafilename

#Initial values for list variables specific to each set of .kel files
A=read_datafilename.get_datafilename()
file=[str(A[0])]
coordinate=[str(A[1])]
print(file)
print(coordinate)

velocityA=[0]         #defines value of first item in array
intensityA=[0]        #defines value of first item in array
stuff=read_parameters.get_limits()
startline=stuff[2]
endline=stuff[3]

os.chdir("data")
for workingfile in file:
    with open(workingfile, 'r') as f:    
        N=0
        for line in f:
            N=N+1
            if N>=startline and N<=endline:
                linestring=line.split()      
                velocity=float(linestring[1])
                velocityA.append(velocity)
                intensity=float(linestring[2])
                intensityA.append(intensity)
    f.closed
    True
    velocityA[0]=velocityA[1]
    intensityA[0]=intensityA[1]

#Get galactic latitude and longitude to display on plot title
gallatlong=read_parameters.get_gallatlong()

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure(figsize=(10,6))
ax=plt.axes()
#title
lat=str(gallatlong[0])
long=str(gallatlong[1])
ax.set_title("Galactic Longitude " + long + " degrees  "+"    Galactic Latitude "+ lat+" degrees")
#label axes
ax.set_xlabel(A[1])
ax.set_ylabel("Intensity_(K)")
#plot array data
ax.scatter(velocityA,intensityA, marker=".", c="red")
plt.show()
os.chdir("..")

