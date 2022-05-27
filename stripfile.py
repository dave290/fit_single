#stripfile.py
#Read .kel file and write velocity and intensity data 
#to a new file with 2, space-delimited columns.
#Uses the file, parameter.txt to read the filename and the
#upper and lower values of velocity (or frequency)

import os
import read_datafilename
import read_parameters

#READ FILENAME AND WRITE NEW NAME
A=read_datafilename.get_datafilename()
datafilename=A[0]
print("Data file to be read ",datafilename)
LDFN=len(datafilename)
newfilename=datafilename[0:LDFN-4]+".txt"

#GET STARTING AND ENDING LINE NUMBERS OF DATA FILE
limits=read_parameters.get_limits()
startline=limits[2]
endline=limits[3]

#WRITE DATA TO NEW FILE
os.chdir("Data")
with open(datafilename, 'r') as f:
    with open(newfilename, 'w') as g:
        N=0
        for line in f:
            N=N+1
            if N>=startline and N<=endline:
                linestring=line.split()
                X=linestring[1]
                rejoin=X+" "+linestring[2]+" " 
                g.write(rejoin)
                g.write('\n')
    g.closed
    True
f.closed
True
print("Data Written to ",newfilename)
os.chdir("..")

