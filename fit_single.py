#fit_single.py
#Fits selected peak from a .kel file with a single gaussian after subtracting linear background
#Format is intensity vs velocity
#David Schultz, December 22,2021

import collections        #needed for deque, remove, & rotate
import os                 #allows use of directory changing & reading commands
import read_datafilename  #reads name of .kel file
import read_datafile      #reads contents of a single .kel file
import read_parameters    #reads fit_parameters.txt
import minimize           #fits center, coefficient & sigma values
import plot               #plots data and final fit

#READ NAME AND TYPE OF .KEL FILE
A=read_datafilename.get_datafilename()
print("\n")
datafilename=A[0]; print("Data file",datafilename)
LDFN=len(datafilename)
newfilename=datafilename[0:LDFN-4]+".dat"
path=os.getcwd()+"/data/"
newfilename=path+newfilename
coordinate=A[1]

#READ USER-DEFINED UPPER AND LOWER THRESHOLDS AND GET THEIR INTENSITIES
limits=read_parameters.get_limits()
lft=limits[0];uft=limits[1]
startline=limits[2];endline=limits[3]
velocity=read_datafile.velocity(startline,endline)
intensity=read_datafile.intensity(startline,endline)
impv=intensity[0]   #intensity of most negative velocity
imnv=intensity[-1]  #intensity of most positive velocity
offset=startline-63 #use this when plotting line superimposed on data

#CALCULATE LINEAR BASELINE SLOPE AND INTERCEPT
delta=imnv-impv
points=len(intensity)
slope=delta/points
intercept=impv

#GET FIT DISPLAY TYPE - SHOWLINE OR SHOWFIT
fitdisplaytype=read_parameters.get_fitdisplay()
print(fitdisplaytype)

if fitdisplaytype=="showline":
    #READ EXPERIMENTAL DATA FROM -200000 M/S to +200000 M/S
    velocity=read_datafile.velocity(63,869)
    intensity=read_datafile.intensity(63,869)
    plot.plot_showline(velocity,intensity,points,slope,intercept,coordinate,offset)
    exit()

if fitdisplaytype=="showfit":
    #GET PARAMETERS AND FLAGS
    params_flags=read_parameters.get_params_flags()
    parameter=params_flags[0]
    print("Initial parameters: center, coefficient, sigma")
    print(parameter)
    
    flag=params_flags[1]
    centerflagA=flag[0];coefflagA=flag[1];sigmaflagA=flag[2]
    print("Flags")
    print(flag)

    #GET ITERATIONS, STARTLINE AND ENDLINE
    total_iterations=read_parameters.get_iterations()
    print("Total Iterations ",total_iterations)
    limits=read_parameters.get_limits()
    lowerfitthreshold=limits[0];upperfitthreshold=limits[1]
    startline=limits[2];endline=limits[3]
    print("Lower fit threshold, upper fit threshold, startline, endline")
    print(limits)

    #GET STEPS AND MAX_PASSES
    steplist=read_parameters.get_step()
    print("Stepsize & Maximum Passes: Center (x2), Coefficient (x2), Sigma (x2)")
    print(steplist)

    #READ EXPERIMENTAL DATA AND SUBTRACT BASELINE
    velocity=read_datafile.velocity(startline,endline)
    intensity=read_datafile.intensity(startline,endline)
    for i in range(points):
        correction=slope*i+intercept
        intensity[i]=intensity[i]-correction

    #EXECUTE ITERATIONS
    print("Differences")
    Z=[99999]
    sumterms=0
    for iterations in range(total_iterations):
        #Fit center***********************************************
        if centerflagA==1: #fit peak A 
            centerA=minimize.center(velocity,intensity,parameter,startline,endline,steplist)
            parameter[0]=centerA[0]
            sumterms=centerA[1]  
        #Fit coefficient******************************************
        if coefflagA==1:
            coefA=minimize.coef(velocity,intensity,parameter,startline,endline,steplist)
            parameter[1]=coefA[0]
            sumterms=coefA[1]
        #Fit sigma************************************************            
        if sigmaflagA==1:
            sigmaA=minimize.sigma(velocity,intensity,parameter,startline,endline,steplist)
            parameter[2]=sigmaA[0]
            sumterms=sigmaA[1]
        Z.append(sumterms)
        if Z[iterations+1]<Z[iterations]:
            print(Z)
        else:
            break
    print("ALL DONE!")
    print("Final parameters")
    print(parameter)
    print("\n") 

    #Write data to dat file
    with open(newfilename, 'w') as g:
        g.write(A[0]);g.write("\n")
        g.write(coordinate);g.write("\n")
        g.write("Fit limits");g.write("\n")
        g.write(str(limits[0:2]));g.write("\n")
        g.write("Final parameters");g.write("\n")
        g.write("Center, Coefficient, Width");g.write("\n")
        g.write(str(parameter[0:3]));g.write("\n")
    g.closed
    True

plot.plot_showfit(velocity,intensity,parameter,startline,endline,coordinate)
exit()
