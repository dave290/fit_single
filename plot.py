#plot.py

import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_showline(velocity,intensity,points,slope,intercept,offset):
    fig=plt.figure(figsize=(10,6))
    ax=plt.axes()
    ax.set_title("Intensity vs Velocity",fontsize=20)
    ax.set_xlabel("Velocity (km/s)",fontsize=18)
    ax.set_ylabel("Intensity (K)",fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    for i in range(points):
        correction=slope*i+intercept
        ax.scatter(velocity[i+offset],correction,marker=".",c="blue")
    ax.scatter(velocity,intensity, marker=".", c="red",s=200)
    plt.show()

def plot_showfit(velocity,intensity,parameter,startline,endline):
    gaussAA=[0]
    #calculate gaussian function
    totallines=endline-startline+1
    for j in range(totallines):
        exponentA=(-1*(velocity[j]-parameter[0])**2)/(2*(parameter[2])**2)
        gaussA=(parameter[1])*(2.718**exponentA)
        gaussAA.append(gaussA)
    gauss_dequed=collections.deque(gaussAA)
    gauss_dequed.remove(0)
    gaussAAA=list(gauss_dequed)   
    
    #plot the data
    fig=plt.figure(figsize=(10,6))
    ax=plt.axes()
    ax.set_title("Intensity vs Velocity",fontsize=20)
    ax.set_xlabel("Velocity (km/s)",fontsize=18)
    ax.set_ylabel("Intensity (K)",fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    #use ax.scatter to plot individual data points
    ax.scatter(velocity,intensity,c="red",s=80)
    #use plt.plot in order to plot a function with lines only
    plt.plot(velocity,gaussAAA,c="blue")
    plt.show()
