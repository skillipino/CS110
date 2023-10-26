import stdarray
import stdrandom
import stdio

#initialize arrays and counter
minuet = stdarray.create2D(11,16,0)
trios = stdarray.create2D(6,16,0)
total = 0

#read from standard input and saves input in 2d array for corresponding minuet or trio
while not stdio.isEmpty():
    if total < 176:
        for i in range(11):
            for j in range(16):
                minuet[i][j] = stdio.readInt()
                total += 1
    else:
        for i in range(6):
            for j in range(16):
                trios[i][j] = stdio.readInt()
                total += 1


#loops through array of len of both arrays column, rolling fair dice to determine measure used and then printing array
for z in range(len(minuet[0]) + len(trios[0])):
    if z < len(minuet):
        i = stdrandom.uniformInt(1,7) + stdrandom.uniformInt(1,7)
        j = stdrandom.uniformInt(0,16)
        stdio.write(str(minuet[i-2][j]) + " ")
    else:
        i = stdrandom.uniformInt(1,7)
        j = stdrandom.uniformInt(0,16)
        if z < len(minuet[0]) + len(trios[0]) - 2:
            stdio.write(str(trios[i-1][j]) + " ")
        else:
            stdio.writeln(str(trios[i - 1][j]))