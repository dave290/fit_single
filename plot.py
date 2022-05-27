#plot.py

import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def plot_showline(velocity,intensity,points,slope,intercept,coordinate,offset):
    fig=plt.figure(figsize=(10,6))
    ax=plt.axes()
    ax.set_title("Intensity_(Kelvins) vs "+coordinate)
    ax.set_xlabel(coordinate)
    ax.set_ylabel("Intensity_(K)")
    for i in range(points):
        correction=slope*i+intercept
        ax.scatter(velocity[i+offset],correction,marker=".",c="blue")
    ax.scatter(velocity,intensity, marker=".", c="red")
    plt.show()

def plot_showfit(velocity,intensity,parameter,startline,endline,coordinate):
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
    ax.set_title("Intensity_(Kelvins) vs "+coordinate)
    ax.set_xlabel(coordinate)
    ax.set_ylabel("Intensity_(K)")
    ax.scatter(velocity,intensity, marker=".", c="red")
    ax.scatter(velocity,gaussAAA, marker=".", c="blue")
    plt.show()
