#created a random word search generator
#Note: allows for the inclusion of x
from random import *
def puzzleGen(size):
        puzzle = [[]*size]*size
        numbers = list(range(97,123))
        shuffle(numbers)
        for i in range(len(numbers)):
                numbers[i] = chr(numbers[i])
        j = 0
        for row in range(size):
                puzzle[row] = numbers[j:(j+size)]
                j += size
                if( j >= size):
                        shuffle(numbers)
                        j = 0
        for i in range(size):
                print(puzzle[i])
