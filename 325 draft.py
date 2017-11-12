from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(Graph):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

def getGrid(size=5):
    
    grid = [[random.choice(string.ascii_lowercase) for c in range(size)] for r in range(size)]
    
    return grid


    def getAdjacentLetters(grid, r, c):
    gsize = len(grid)
    
    neighbors = [ [(r-1,c-1),(r-1,c),(r-1,c+1)],
                   [(r,c-1),          (r,c+1)],
                   [(r+1,c-1),(r+1,c) ,(r+1,c+1)] ]

    
    # if we are on the edge column of the grid
    if c == 0:
        # left edge -> keep the 2 rightmost columns
        res = [n[1:] for n in neighbors]
    elif c == gsize-1:
        # right edge -> keep the two leftmost columns
        res = [neighbors[0][0:2], [neighbors[1][0]], neighbors[2][0:2]]
    else:
        # somewhere in the grid, keep everything
        res = neighbors
    
    if r == 0:
        # top edge of the grid -> keep the bottom two rows 
        res = res[1:]
    elif r == gsize-1:
        # bottom edge -> keep the top two rows
        res = res[0:2]
    else:
        pass
    
    letters = []
    for row in res:
        letters.extend( [(grid[r][c],r,c) for r,c in row] )

    return letters
