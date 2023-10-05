#Daniel Nocon
#Project 2
#Problem 2. (Day of the Week ) Write a program called day_of_week.py that accepts m (int), d (int), and y (int) as command-line
#arguments, computes the day of the week (0 for Sunday, 1 for Monday, and so on) dow using the formulae below, and writes
#the day as a string (“Sunday”, “Monday”, and so on) to standard output.

#y0 = y − (14 − m)/12,
#x0 = y0 + y0/4 − y0/100 + y0/400,
#m0 = m + 12 × ((14 − m)/12) − 2,
#dow = (d + x0 + 31 × m0/12) mod 7.

import stdio
import sys

#stores command line args in variables
m = int(sys.argv[1]) #m = month
d = int(sys.argv[2]) #d = day
y = int(sys.argv[3]) #y = year

#uses command line variables to calculate the day of the week
y0 = y - (14 - m)//12
x0 = y0 + y0//4 -y0//100 + y0//400
m0 = m + 12 * ((14-m)//12) - 2
dow = int((d + x0 + 31 * m0//12) % 7)

#control flow if statements, prints corresponding day of week to number value resulting in dow formula
if(dow == 0):
    stdio.writeln("Sunday")
elif(dow == 1):
    stdio.writeln("Monday")
elif(dow == 2):
    stdio.writeln("Tuesday")
elif (dow == 3):
    stdio.writeln("Wednesday")
elif (dow == 4):
    stdio.writeln("Thursday")
elif (dow == 5):
    stdio.writeln("Friday")
else:
    stdio.writeln("Saturday")
