#Daniel Nocon
#Project 2
#Problem 1. (Wind Chill ) Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National
#Weather Service defines the effective temperature (the wind chill) to be
#w = 35.74 + 0.6215t + (0.4275t − 35.75)v0.16.
#Write a program called wind_chill.py that accepts t (float) and v (float) as command-line arguments, and writes the wind chill
#w to standard output. Your program should report the message “Value of t must be ≤ 50 F” if t > 50, and the message
#“Value of v must be > 3 mph” if v ≤ 3.

import stdio
import sys

#assigning variables
t = float(sys.argv[1]) #stores command line argument 1 to t
v = float(sys.argv[2]) #stores command line argument 2 to v
w = 0

#control flow if statements
if(t > 50): #checks that value of t
    stdio.writeln("Value of t must be <= 50 F") #if not equal to or less than 50, prints message to screen
elif(v <= 3):#if t in range, checks value of v
    stdio.writeln("Value of v must be > 3 mph") #if not greater than 3, prints message to screen
else:#if t and v are in range, it calculates wind chill using NWS formula
    w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * v**0.16)
    stdio.writeln(w)#prints resulting value of w to screen
