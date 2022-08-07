#read_parameters.py

import os
import collections
import read_datafilename

def get_fitdisplay():
    os.chdir('data')
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="F":     
                    fitdisplay=linestring[1]
        f.closed
        True
    os.chdir("..")
    return fitdisplay

def get_params_flags():
    os.chdir('data')
    file=["parameters.txt"]
    parameter=[0];flag=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0]=="P":     
                    parametertemp=float(linestring[2])
                    parameter.append(parametertemp)
                    flagtemp=int(linestring[3])
                    flag.append(flagtemp)
        f.closed
        True
    parameter_dequed=collections.deque(parameter)
    parameter_dequed.remove(0)
    parameter=list(parameter_dequed)
    flag_dequed=collections.deque(flag)
    flag_dequed.remove(0)
    flag=list(flag_dequed)
    os.chdir("..")
    return parameter,flag

def get_step():
    os.chdir('data')
    file=["parameters.txt"]
    step=[0]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "S":      
                    steptemp1=float(linestring[2])
                    steptemp2=int(linestring[3])
                    step.append(steptemp1)
                    step.append(steptemp2)
        f.closed
        True
    step_dequed=collections.deque(step)
    step_dequed.remove(0)
    step=list(step_dequed)
    os.chdir("..")
    return step

def get_iterations():
    os.chdir('data')
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "Iterations":      
                    iterations=int(linestring[1])          
        f.closed
        True
    os.chdir("..")
    return iterations

def get_limits():
    #read lower and upper fit thresholds
    os.chdir('data')
    file=["parameters.txt"]
    for workingfile in file:
        with open(workingfile,'r') as f:
            for line in f:
                linestring=line.split()
                if linestring[0] == "Lowerfitthreshold":      
                    lowerfitthreshold=float(linestring[1])
                if linestring[0] == "Upperfitthreshold":
                    upperfitthreshold=float(linestring[1])             
        f.closed
        True
    os.chdir("..")
    #determine starting and ending line numbers from data file
    A=read_datafilename.get_datafilename()
    datafile=[A[0]]
    os.chdir("data")
    for workingfile in datafile:
        with open(workingfile, 'r') as f:  
            linesofdata=[0]
            line_no=0
            for line in f:
                line_no=line_no+1
                linestring=line.split()
                if linestring[0]=="#":
                    pass
                else:
                    velocity=float(linestring[1])
                    if velocity>=lowerfitthreshold and velocity<=upperfitthreshold:
                        linesofdata.append(line_no)
        f.closed
        True
    startline=int(linesofdata[1])
    endline=int(linesofdata[-1])
    limits=[lowerfitthreshold,upperfitthreshold,startline,endline]
    os.chdir("..")
    return limits

def get_gallatlong():
    #read galactic latitude and longitude values saved in .kel file header
    os.chdir("..")
    A=read_datafilename.get_datafilename()
    file=str(A[0])
    os.chdir("data")
    colon=[999]
    with open(file, 'r') as f:
        for line in f:
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
        f.closed
        True
    os.chdir("..")
    gallatlong=[gallat,gallon]
    return gallatlong
