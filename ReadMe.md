Welcome!  This suite of Python scripts is intended to be used for fitting 
radio-astronomical data obtained from the NsfIntegrate program.

fit_single.py allows you to fit a scan with a single gaussian peak,
with the ability to subtract a linear baseline

SETTING UP THESE PROGRAMS FOR THE FIRST TIME
The Matplotlib program is required for plotting. PIP install using the command below:
$ pip install matplotlib
The subfolder "data" should contain the programs below.
parameters.txt
plotvel.py
<datafile>.kel

DETERMINE THE ENDPOINTS OF THE LINEAR BASELINE
Go to subfolder "data"
View the intensity vs velocity data contained in the .kel file using the command below:
$ python plotvel.py
Use this plot to estimate the lower and upper bounds of velocity you will use for your linear baseline
Open the file "parameters.txt"  (leave this file open so you can modify later)
On line 3, enter the name of the kel file that you wish to fit.
Make sure this file is also in the "data" subfolder.
Set values for lower and upper fit threshold velocities in km/s
In the "S" lines, enter the stepsizes and maximum allowed steps
Enter "showline" on the line with a "F" header
Save "parameters.txt" after you have made your changes.

Return to folder "fit_single"
Enter the command below:
$ python fit_single.py
A blue line will appear. This is the baseline you have selected.
In the parameters file, adjust lower and upper fit values until blue line matches edges of the peak,
and repeat until you have an acceptable baselien.

FIND THE CENTER, COEFFICIENT AND HEIGHT OF THE PEAK YOU SELECTED
When you're satisfied with the baseline, enter "showfit" on the "F" line of "parameters.txt"
In "parameters.txt" enter your approximate guesses for the peak center, coefficient and width
Set the flag next to each to "1" to fit, or "0" to keep constant.
Enter the command below:
$ python fit_single.py
After running, the program will display the fit to your data.
It will display your best-fit values in the terminal window and store them in a .dat file.
