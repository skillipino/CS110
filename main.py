#Daniel Nocon
#Exercise 3
#PProblem 1. (Birthday Problem) Suppose that people enter an empty room until a pair of people share a birthday. On
#average, how many people will have to enter before there is a match? Write a program called birthday.py that accepts trials
#(int) as command-line argument, runs trials experiments to estimate this quantity — each experiment involves sampling
#individuals until a pair of them share a birthday, and writes the value to standard output

import stdio
import sys
import stdarray
import stdrandom

trials = int(sys.argv[1])
birthdayList = stdarray.createID[31, False]
trialRuns = 0
inRoom = 0
total = 0

for i in range(0, trials):
    match = False
    while match == False:
        bday = stdrandom.uniformInt(0,31)
        inRoom += 1
        if birthdayList[bday] == False:
            birthdayList[bday] = True
        elif birthdayList[bday] == True:
            total += inRoom
            match = True
            break

avg = total//trials
stdio.writeln(avg)
