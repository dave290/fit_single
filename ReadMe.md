Welcome!  This suite of Python scripts is intended to be used for fitting radio-astronomical data obtained from the NsfIntegrate program.

The Matplotlib program is required for plotting. PIP install using the command below:
$ pip install matplotlib

Be sure to create a folder named "Data" and make this a subfolder inside of the folder containing the programs below.
The Data folder should contain the following two files:
parameters.txt
<datafile>.kel

In Data, open the file PARAMETERS.TXT
Enter the .kel file name on line 5
Enter the lower and upper fit threshold values on lines 7 & 8
Enter showline on line 12

Return to the parent folder containing the Python scripts
Open terminal window in this folder
Type command
  python fit_single.py
Plot will show a blue line showing the linear baseline to be subtracted.
Go back to the parameter file to adjust the start and end-points of this line
so that the baseline makes sense.

When baseline is good, then go back to line 12 in the parameter file
and enter showfit
Enter best guesses for initial fit values
Set flags to 0 or 1 depending on if you wish to optimize each parameter.
Run program again

When you're done, the following files will be generated:
.dat file (contains final parameters)
.png file (image of data with fit)




