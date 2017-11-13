#The function times how long it takes to find all the letters in an alphanumeric sequence.
from random import *
from pythonds import Graph, Vertex
from string import ascii_lowercase

#---------------------------------------------PUZZLE GENERATOR------------------------------------------------------------
# creates a n-by-n puzzle consisting or random letters
def puzzleGen(size = 8):
        puzzle = [[choice(ascii_lowercase) for c in range(size)] for r in range(size)]
        return puzzle
#creates the graph that will be used to run DFS
def createBoard(size = 8):
        game = Graph()
        for row in range(size):
                for col in range(size):
                        ID = (row*size) + col
                        pos = moves(row,col,size)
                        for i in pos:
                                nid = (i[0]*size) + i[1]
                                game.addEdge(ID, nid)
        return game
#matches the cell in the generated puzzle with the
#node in the generated graph of a n-by-n puzzle
def matches(grid, size = 8):
        pairs = {}
        vertex = 0
        for row in range(size):
                for col in range(size):
                        pairs[vertex] = grid[row][col]
                        vertex += 1
        return pairs

#---------------------------------------------------------SEARCH TERMS-------------------------------------------------------
#take the given input and breaks it down into
#the unique characters that need to be found
def getLetters(string):
        string = string.split(" ")
        search = {}
        for index in range(len(string)):
                for i in range(len(string[index])):
                        search[string[index][i]]= False
        return search

#checks if all the search values have been found
def checkFinished(charList):
        finished = True
        for key in charList:
                if not charList[key]:
                        finished = False
                        break
        return finished

#------------------------------------------------------------MOVES REGULATION-----------------------------------------
#creates the moves that are allowed in the game
#uses the same setup as the knight's problem
def moves(x, y, size):
        newMoves = []
####        offsets = [(-1, -2), (-1, 2), (1, -2), (1, 2),
##                        (-2, -1), (-2, 1), (2, -1), (2, 1)]
        offsets = [  (-1, -1), (-1, 0), (-1, 1),
                        (0, -1), (0, 1),
                        (1, -1), (1, 0), (1, 1)]
        for m in offsets:
                X = x + m[0]
                Y = y + m[1]
                if legalCoord(X, size) and legalCoord(Y, size):
                        newMoves.append((X, Y))
                return newMoves
#checks whether the coordinates exists on the board
def legalCoord(x, size):
        if x >= 0 and x < size: return True
        else: return False

#---------------------------------------------------DEPTH FIRST SEARCH------------------------------------
def play(graph, string):
        search = getLetters(string)
        puzzle = puzzleGen(8)
        couples = matches(puzzle)
        for aVertex in graph:
                aVertex.setColor('white')
                aVertex.setPred(-1)
        for aVertex in graph:
                if aVertex.getColor() == 'white':
                        if search.get(couples[aVertex.id]) != None:
                                search[couples[aVertex.id]] = True
                        dfsvisit(graph, aVertex)
                if checkFinished(search): break
        if not checkFinished(search):
                print("Not all characters found for '",string,"'")
        else:
                print("All characters for '",string,"' were found.")

def dfsvisit(graph, startVertex):
        startVertex.setColor('gray')
        for nextVertex in startVertex.getConnections():
                if nextVertex.getColor() == 'white':
                        nextVertex.setPred(startVertex)
                        dfsvisit(graph, nextVertex)
        startVertex.setColor('black')

#-------------------------------------------------------MAIN---------------------------------------------------------
play(createBoard(), "eboni")
play(createBoard(), "carmen")
