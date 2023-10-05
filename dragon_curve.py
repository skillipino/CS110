#Daniel Nocon
#Project 2
#Problem 8. (Dragon Curve) The instructions for drawing a dragon curve are strings of the characters F , L, and R, where
#F means “draw a line while moving 1 unit forward”, L means “turn left”, and R means “turn right”. The key to solving
#this problem is to note that a curve of order n is a curve of order n − 1 followed by an L followed by a curve of order n − 1
#traversed in reverse order, replacing L with R and R with L. Write a program called dragon_curve.py that accepts n (int) as
#command-line argument, and writes to standard output the instructions for drawing a dragon curve of order n.

import stdio
import sys

#assigning variables
n = int(sys.argv[1]) #accepts command line argument as n
dragon = str("F") #stores string F to variable dragon
nogard = str("F") #stores string F to variable nogard

#control flow for statement
for i in range(1,n+1): #iterates through for statement until i == n
    temp1 = dragon #stores string dragon to temp1
    temp2 = nogard #stores string nogard to temp 2
    dragon = temp1 +"L" + temp2 #reassigns dragon to old dragon string + L + old nogard string
    nogard = temp1 + "R" + temp2 #reassigns nogard to old dragon string + R + old nogard string

#prints entire dragon string to screen after exiting for loop
stdio.writeln(dragon)
