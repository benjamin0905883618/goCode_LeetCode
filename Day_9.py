import sys

class Solution:

    # @param grid: List[List[int]]
    # @return int
    def findMaxIslandArea(self, grid):
        # Implement me
        x_size = len(grid[0])
        y_size = len(grid)
        max_place = 0
        for y in range(y_size):
            for x in range(x_size):
                #print(x,y)
                if grid[y][x] == 0:
                    continue
                else:
                    temp_place = find_island_size(grid,x,y)
                    #print(temp_place)
                    if temp_place > max_place:
                        max_place = temp_place
        return max_place
        
def find_island_size(grid,x,y,size = 0):
    grid[y][x] = 0
    new_size = size + 1
    if x - 1 >= 0 and grid[y][x - 1] == 1:
        new_size = find_island_size(grid,x - 1,y,new_size)
    if y - 1 >= 0 and grid[y - 1][x] == 1:
        new_size = find_island_size(grid,x,y - 1,new_size)
    if x + 1 < len(grid[0]) and grid[y][x + 1] == 1:
        new_size = find_island_size(grid,x + 1,y,new_size)
    if y + 1 < len(grid) and grid[y + 1][x] == 1:
        new_size = find_island_size(grid,x,y + 1,new_size)
    return new_size


grid = [[0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0]]
#print(len(grid))
#print(len(grid[0]))

s = Solution()
print(s.findMaxIslandArea(grid))
