#Daniel Nocon
#Project 2
#Problem 7. (Sum of Powers) Write a program called sum_of_powers.py that accepts n (int) and k (int) as command-line
#arguments, and writes to standard output the sum 1k + 2k + · · · + nk.

import stdio
import sys

#assigning variables
n = int(sys.argv[1]) #stores first command line argument as n
k = int(sys.argv[2]) #stores second command line argument as k
total = 0 #sets variable total to 0

#control flow for statement
for i in range(1,n+1): #loops starting at 1 until i == n
    total += i**k #total is the sum of total + i to the k power until loop ends

#prints the value of total to the screen
stdio.writeln(total)