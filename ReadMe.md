Welcome!  This suite of Python scripts is intended to be used for fitting radio-astronomical data obtained from the NsfIntegrate program.

SETTING UP THESE PROGRAMS FOR THE FIRST TIME
The Matplotlib program is required for plotting. PIP install using the command below:
$ pip install matplotlib
The subfolder "data" should contain the programs below.
parameters.txt
<datafile>.kel
(Be sure to delete the file "Delete_this_File" after updating with a git pull command)

PLOT THE KEL FILE
In "data" subfolder, open the file "parameters.txt"  (leave this file open so you can modify later)
Enter the .kel file name on line 5
Enter lower and upper fit threshold values of -199000 and +199000 on lines 7 & 8
Return to folder "fit_single" and enter command below to plot the .kel file:
$ python plotkel.py

DETERMINE YOUR LINEAR BASELINE TO SUBTRACT FOR A SELECTED PEAK
Now, you're ready to determine the endpoints of the linear baseline you wish to subtract
On lines 7 & 8 of "parameters.txt" enter the lower and upper values based on the left and right sides of the peak you wish to fit
Enter "showline" on line 12
To see the baseline that this will subtract, enter the command below:
$ python fit_single.py
A blue line will appear. This is the baseline you have selected.
Adjust lower and upper fit values until blue line matches edges of the peak.

FIND THE CENTER, COEFFICIENT AND HEIGHT OF THE PEAK YOU SELECTED
When you're satisfied with the baseline, enter "showfit" on line 12 of "parameters.txt"
In "parameters.txt" enter your approximate guesses for the peak center, coefficient and width"
Set the flag next to each to "1" to fit, or "0" to keep constant.
Enter the command below:
$ python fit_single.py
After running, the program will display the fit with the raw data. 
It will display store your best-fit values in the terminal window and store them in a .dat file.
