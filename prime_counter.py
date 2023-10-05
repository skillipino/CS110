#Daniel Nocon
#Exercise 2
#Problem 5. (Counting Primes) Write a program called prime_counter.py that accepts n (int) as command-line argument, and
#writes to standard output the number of primes less than or equal to n.

import stdio
import sys
import math

#assign variables
n = int(sys.argv[1]) #assign command line argument as variable n
p = 2 #counter for prime numbers, starts at 2 to count 2 and 3

#for loop to test primality of numbers
for i in range(n, 1, -1): #outer for loop iterates through all numbers through n
    c = 0 #counter for divisibilty, sets c to 0 for each iteration
    if i % 2 == 0 or i % 3 == 0:
        continue
    else:
        for j in range(4,int(math.sqrt(i))+1): #inner for loop tests for primality of each number i, up to sqrt of i
            if i % j == 0:
                c += 1 # if i modded by j is evenly divisible, c is incremented by 1
        if (c<1):#if c is 0 then number is prime and p is incremented by 1
            p += 1

#prints to screen number of prime numbers
stdio.writeln(p)
