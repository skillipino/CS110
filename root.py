#Daniel Nocon
#Project 2
#Problem 4. (Root Finding) Write a program called root.py (a variant of the sqrt.py program we dicussed in class) that accepts
#k (int), c (float), and epsilon (float) as command-line arguments, and writes to standard output the kth root of c, up to
#epsilon decimal places.

import stdio
import sys

#assigning variables for command line arguments
k = int(sys.argv[1]) # k is int variable for argument 1
c = float(sys.argv[2]) #c is float variable for argument 2
epsilon = float(sys.argv[3]) #epsilon is float variable for argument 3

#sets t to value of variable c
t = c

#control flow while statement
while (1 - (c/(t**k))) > epsilon: #compares the value of (1 - c/t^k) to the value of epsilon
    t = (t-(((t**k)-c)/(k*(t**(k-1))))) #changes value of t to (t - (f(t)/f'(t)) as long as (1 - c/t^k) is greater than epsilon

#prints root (t) to screen
stdio.writeln(t)