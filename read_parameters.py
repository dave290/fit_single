#read_parameters.py

import os
import collections
import read_datafilename

def get_fitdisplay():
    os.chdir('Data')
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
    os.chdir('Data')
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
    os.chdir('Data')
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
    os.chdir('Data')
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
    os.chdir('Data')
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
    os.chdir("Data")
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
