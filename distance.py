#Problem 1. (5 Points) Create a program called distance.py that takes four floats x1, y1, x2, and y2 as command-line arguments
#representing the Cartesian coordinates of two points (x1, y1) and (x2, y2) on a plane, and writes the Euclidean distance between
#the points, calculated as p(x1 − x2)2 + (y1 − y2)2. Enter the following starter code in the program and replace the ellipsis
#(...) with your code.

import math
import stdio
import sys

#accepts command line arguments as float variables
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

#calculates euclidean distance using  sqrt(x1 − x2)2 + (y1 − y2)2
eucdist = math.sqrt(((x1 - x2)**2 + ((y1 - y2)**2)))

#prints result to standard output
stdio.writeln(eucdist)