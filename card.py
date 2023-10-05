#Daniel Nocon
#Project 2
#Problem 3. (Playing Card ) Write a program called card.py that simulates the selection of a random card from a standard
#deck of 52 playing cards, and writes it to standard output.

import stdio
import stdrandom #importing to imitate pulling a random card

#assigning variables for card and suit
rank = stdrandom.uniformInt(2,15) #assigns the value of the card
suit = stdrandom.uniformInt(1,5) #assigns the suit of the card

#control flow if statement to convert value of card to string
if rank == 2:
    rankStr = "2"
elif rank == 3:
    rankStr = "3"
elif rank == 4:
    rankStr = "4"
elif rank == 5:
    rankStr = "5"
elif rank == 6:
    rankStr = "6"
elif rank == 7:
    rankStr = "7"
elif rank == 8:
    rankStr = "8"
elif rank == 9:
    rankStr = "9"
elif rank == 10:
    rankStr = "10"
elif rank == 11:
    rankStr = "Jack"
elif rank == 12:
    rankStr = "Queen"
elif rank == 13:
    rankStr = "King"
else:
    rankStr = "Ace"

#control flow if statement to convert value to suit of card
suit = stdrandom.uniformInt(1,5)
if suit == 1:
    suitStr = "Clubs"
elif suit == 2:
    suitStr = "Diamonds"
elif suit == 3:
    suitStr = "Hearts"
else:
    suitStr = "Spades"

#prints the string conversion of rank and suit to a card from standard 52 card deck
stdio.writeln(rankStr + " of " + suitStr)