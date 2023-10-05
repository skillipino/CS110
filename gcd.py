#Daniel Nocon
#Project 2
#Problem 5. (Greatest Common Divisor ) Write a program called gcd.py that accepts p (int) and q (int) as command-line
#arguments, and writes to standard output the greatest common divisor (gcd) of p and q.

import stdio
import sys

#assigning command line arguments as variables
p = int(sys.argv[1])
q = int(sys.argv[2])

#control flow while statement
while (p % q) != 0: #loop continues until p modded by q = 0
    temp = q #saves value of q to temp
    q = p%q #q is reassigned to the result of p%q
    p = temp #p is assigned to old value of q

#prints the greatest common divisor saved under q
stdio.writeln(q)