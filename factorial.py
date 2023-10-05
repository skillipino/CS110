#Daniel Nocon
#Exercise 2
#Problem 4. Write a program called factorial.py that accepts n (int) as command-line argument, and writes to standard
#output the value of n!, which is defined as n! = 1 × 2 × . . . (n − 1) × n. Note that 0! = 1.

import stdio
import sys

#assigning variables
n = int(sys.argv[1]) #stores command line argument as int variable
i = 1 #variable used as a counter for while statement
f = 1 #variable used to store the calculation for factorial

#control flow while loop
while i < n+1: #terminates loop after it reaches value of n + 1
    f = f * i #saves value of f * i and then multiplies that value by the next increment of i until loop terminates
    i += 1 #counter increments by 1 each iteration until value n+1 has been reached

#prints value of f after termination of while loop
stdio.writeln(f)