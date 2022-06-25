#read_file.py

import os
import collections
import read_parameters
import read_datafilename

def velocity(startline,endline):
    A=read_datafilename.get_datafilename()
    os.chdir('data')
    file=[A[0]]
    vel_list=[0]
    for workingfile in file:
        with open(workingfile, 'r') as f:    
            line_no=0
            for line in f:
                line_no=line_no+1
                if line_no>=startline and line_no<=endline:
                    linestring=line.split()      
                    vel=float(linestring[1])
                    vel_list.append(vel)
        f.closed
        True
    dequed_vel_list=collections.deque(vel_list)
    dequed_vel_list.remove(0)
    velocity=list(dequed_vel_list)
    os.chdir("..")
    return velocity

def intensity(startline,endline):
    A=read_datafilename.get_datafilename()
    os.chdir('data')
    file=[A[0]]
    int_list=[0]
    for workingfile in file:
        with open(workingfile, 'r') as f:    
            line_no=0
            for line in f:
                line_no=line_no+1
                if line_no>=startline and line_no<=endline:
                    linestring=line.split()      
                    int=float(linestring[2])
                    int_list.append(int)
        f.closed
        True
    dequed_int_list=collections.deque(int_list)
    dequed_int_list.remove(0)
    intensity=list(dequed_int_list)
    os.chdir("..")
    return intensity
