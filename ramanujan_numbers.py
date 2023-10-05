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

n = int(sys.argv[1])
a = 1
b = 12
c = 2
d = 11

#while 1 <= a*a*a <= n:

   # while a*a*a + 1 <= b*b*b <= n-a*a*a:

        #while a*a*a + 1 <= c*c*c <= n:

           # while c*c*c + 1 <= d*d*d <= n-c*c*c:
for i in range(1729, n+1):
    b = int(i ** (1 / 3))
    a = int((n - b * b * b) ** (1 / 3))
    c = a + 1
    d = b
    print(1)
    while (c*c*c + d*d*d != i):
        print(2)
        for j in range(c,d):

            if j*j*j + d*d*d == i:
                c = j
                break
            else:
                d -= 1
        if a * a * a + b * b * b == c * c * c + d * d * d:
            total = (a * a * a + b * b * b)
            stdio.writeln(
                str(total) + " = " + str(a) + "^3" + " + " + str(b) + "^3" + " = " + str(c) + "^3" + " + " + str(d) + "^3")



