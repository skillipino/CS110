import stdaudio
import stdio
import sys

#initialize array
waltz = []

#read standard input to array waltz while something to read
while not stdio.isEmpty():
        waltz = stdio.readAllInts()

#tests conditions of array, exit system if not 32 measures, or minuet measure outside range [1,176]
#or trio outside range [1,96]
if len(waltz) != 32:
    sys.exit("A waltz must contain exactly 32 measures")
for i in range(16):
    if waltz[i] < 1 or waltz[i] > 176:
        sys.exit("A minuet measure must be from [1,176]")
for i in range(16,32):
    if waltz[i] < 1 or waltz[i] > 96:
        sys.exit("A trio measure must be from [1,96]")

#loops through range of waltz length, playing the corresponding audio file in the array
for i in range(len(waltz)):
    f = str("data/M") + str(waltz[i])
    stdaudio.playFile(f)
#flushes out audio by waiting for all audio to stop playing
stdaudio.wait()