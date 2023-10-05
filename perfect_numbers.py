#Daniel Nocon
#Project 2
#Problem 9. (Perfect Numbers) A perfect number is a positive integer whose proper divisors add up to the number. For
#example, 6 is a perfect number since its proper divisors 1, 2, and 3 add up to 6. Write a program called perfect_numbers.py that
#accepts n (int) as command-line argument, and writes to standard output the perfect numbers that are less than or equal to
#n.

import stdio
import sys

#assigning variables
n = int(sys.argv[1]) #stores command line argument as n

#control flow nested for statements
for i in range(2,n+1): #outer for loop, starting at 2, ending at n
    total = 0 #sets total (sum of divisors of i) to 0
    for j in range(1,i//2+1): #inner for loop, starting at 1, ending at i/2 (int division) + 1
        if i % j == 0: #executes when i%j == 0
            total += j #increments total by value of j
    if total == i: #control flow if statement, executes when total == i after exiting inner for loop
        stdio.writeln(i) #prints the value of i and goes to next line
