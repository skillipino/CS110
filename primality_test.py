#Daniel Nocon
#Exercise 2
#Problem 3. (Primality Test) Write a program called primality_test.py that accepts n (int) as command-line argument, and
#writes to standard output if n is a prime number or not.

import stdio
import sys
import math

#assign variables
n = int(sys.argv[1]) #assign command line argument as variable n
count = 0 #counter for # of values that evenly divide n

#control flow statements
if n < 2: #1 is not prime so
    stdio.writeln("False")
else:
    for i in range(2, int(math.sqrt(n)+1)): #testing up to sqrt of n, if theres a number divisible other than 1 it is not prime, this makes the program more efficient
        if n % i == 0:
            count +=1 #increments count when n is evenly divisible by i
            if count > 0: #checks count to see if prime, over 1 is not prime
                stdio.writeln ("False")
                break
    if count == 0:
        stdio.writeln("True")




