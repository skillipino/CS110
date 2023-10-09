#Daniel Nocon
#Project 2
#Problem 10. (Ramanujan Numbers) Srinivasa Ramanujan was an Indian mathematician who became famous for his intuition
#for numbers. When the English mathematician G. H. Hardy came to visit him one day, Hardy remarked that the number of
#his taxi was 1729, a rather dull number. Ramanujan replied, “No, Hardy! It is a very interesting number. It is the smallest
#number expressible as the sum of two cubes in two different ways.” Verify this claim by writing a program ramanujan_numbers.py
#that accepts n (int) as command-line argument, and writes to standard output all integers less than or equal to n that can
#be expressed as the sum of two cubes in two different ways. In other words, find distinct positive integers a, b, c, and d such
#that a**3 + b**3 = c**3 + d**3 ≤ n.

import stdio
import sys

#assigning command line arg to variable
n = int(sys.argv[1])
a = 1

#nested while loops
while 1 <= a*a*a <= n:
    b = a + 1
    while a*a*a + 1 <= b*b*b <= n-a*a*a:
        c = a + 1
        while a*a*a + 1 <= c*c*c <= n:
            d = c + 1
            while c*c*c + 1 <= d*d*d <= n-c*c*c:
                x = a*a*a + b*b*b
                y = c*c*c + d*d*d
                if x==y: #checks that the sum of both factors are equal
                    total = (a * a * a + b * b * b)
                    stdio.writeln(str(total) + " = " + str(a) + "^3" + " + " + str(b) + "^3" + " = " + str(c) + "^3" + " + " + str(d) + "^3")
                d += 1
            c += 1
        b += 1
    a += 1