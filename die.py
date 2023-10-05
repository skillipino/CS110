#Daniel Nocon
#Exercise 2
#Problem 2. (Six-sided Die) Write a program called die.py that simulates the roll of a six-sided die, and writes to standard
#output the pattern on the top face.

import stdio
import stdrandom

#using stdrandom library to simulate a 6 sided die roll
r = stdrandom.uniformInt(1,7)

#using control flow if statements to display the result stored in r as a die face
if(r==1):
    stdio.writeln("     ")
    stdio.writeln("  *  ")
    stdio.writeln("     ")
elif (r==2):
        stdio.writeln("*    ")
        stdio.writeln("     ")
        stdio.writeln("    *")
elif (r==3):
        stdio.writeln("*    ")
        stdio.writeln("  *  ")
        stdio.writeln("    *")
elif (r==4):
        stdio.writeln("*   *")
        stdio.writeln("     ")
        stdio.writeln("*   *")
elif (r==5):
        stdio.writeln("*   *")
        stdio.writeln("  *  ")
        stdio.writeln("*   *")
elif (r==6):
        stdio.writeln("*   *")
        stdio.writeln("*   *")
        stdio.writeln("*   *")


