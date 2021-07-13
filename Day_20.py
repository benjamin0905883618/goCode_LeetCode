class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Solution:
    
    # @param maze: List[List[int]]
    # @param A: List[int]
    # @param B: List[int]
    # @return str
    def findShortestPath(self, maze, A, B):
        # Implement me
        answer = []
        answer = playing_maze(maze,A,B,answer)
        print_all_route(answer)

def playing_maze(map,begin,terminate,route):
    map[begin.x][begin.y] = 1
    if map[terminate.x][terminate.y] == 1:
        route.append(begin)
        return route
    route.append(begin)
    #check top
    if begin.x - 1 >= 0 and map[begin.x - 1][begin.y] == 0:
        #print("go top",end = " ")
        temp = Coordinate(begin.x - 1, begin.y)
        route = playing_maze(map,temp,terminate,route)
        if map[terminate.x][terminate.y] == 1:
            return route
    #check left
    if begin.y - 1 >= 0 and map[begin.x][begin.y - 1] == 0:
        #print("turn left",end = " ")
        temp = Coordinate(begin.x, begin.y - 1)
        route = playing_maze(map,temp,terminate,route)
        if map[terminate.x][terminate.y] == 1:
            return route
    #check bottom
    if begin.x + 1 < len(map) and map[begin.x + 1][begin.y] == 0:
        temp = Coordinate(begin.x + 1, begin.y)
        route = playing_maze(map,temp,terminate,route)
        if map[terminate.x][terminate.y] == 1:
            return route
    #check right
    if begin.y + 1 < len(map[0]) and map[begin.x][begin.y + 1] == 0:
        temp = Coordinate(begin.x, begin.y + 1)
        route = playing_maze(map,temp,terminate,route)
        if map[terminate.x][terminate.y] == 1:
            return route

def print_coor(point,end = False):
    if end == False:
        print("( %d, %d )"%(point.x,point.y))
    else:
        print("( %d, %d )"%(point.x,point.y),end = " ")
def print_all_route(route):
    if route:
        for i in route:
            print_coor(i,True)
        print()
    else:
        print("")

maze = [
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 0, 0, 0, 1]]
A = Coordinate(0,0)
B = Coordinate(0,2)
s = Solution()
s.findShortestPath(maze,A,B)
