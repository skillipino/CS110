#Daniel Nocon
#Exercise 2
#Problem 1 (Quadratic Equation) Write a program called quadratic.py (a variant of the program we discussed in class) that
#accepts a (float), b (float), and c (float) as command-line arguments, and writes to standard output the roots of the quadratic
#equation ax2 + bx + c = 0. Your program should report the message “Value of a must not be 0” if a = 0, and the message
#“Value of discriminant must not be negative” if b2 − 4ac < 0.

import stdio
import sys
import math

#assign command line arguments as float variables
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

#calculation for discriminant in quadratic equation
d = b**2 - (4*a*c)

#control flow statements to ensure roots are calculated, first checks to make sure not dividing by 0,
#then checks to make sure the discriminant is greater than 0, if both conditions are okay it calculates
#and prints the resulting roots
if(a==0):
    stdio.writeln("Value of a must not be 0")
elif(d<0):
    stdio.writeln("Value of discriminant must not be negative")
else:
    root1 = ((-b) + math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    root2 = ((-b) - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    stdio.writeln(str(root1) + " " + str(root2))