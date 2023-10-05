#Daniel Nocon
#Project 2
#Problem 6. (Fibonacci Number ) Write a program called fibonacci.py that accepts n (int) as command-line argument, and
#writes to standard output the nth number from the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, . . . ).

import stdio
import sys

#assigning variables
n = int(sys.argv[1]) #stores command line argument to n
a = 1 #first number in fibonacci sequence
b = 1 #second number in fibonacci sequence
i = 3 #first spot in fibonacci sequence after a and b

#control flow while statement
while i <= n: #while i is less than nth number of fibonacci seq
    temp = b #stores value of b in temp variable
    b = a + b #b reassigned to value of a + b
    a = temp #a reassigned to old value of b
    i += 1 #i increments by 1 until equal to n

#prints b which is now the nth number in fibonacci sequence
stdio.writeln(b)