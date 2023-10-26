#Problem 2. (10 Points) Create a program called minmax.py that accepts integers from standard input and writes their minimum
#and maximum values to standard output. Enter the following starter code in the program and replace the ellipsis (...) with
#your code.

import stdio

#initializes array num and then stores standard input into array
num = []
num = stdio.readAllInts()
#initializes min and max variables to the first element of array
min = None
max = None

#loops through array checking each element against the current min and max and saving the value if it is smaller or
# larger than current value
for i in range(len(num)):
    if min == None:
        min = num[i]
    elif num[i] < min:
        min = num[i]
    if max == None:
        max = num[i]
    elif num[i] > max:
        max = num[i]

#takes min and max values and writes result to screen
stdio.writeln("Minimum = " + str(min))
stdio.writeln("Maximum = " + str(max))