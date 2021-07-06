"""
這道題目曾出現在 Amazon 的面試中。

給定一個三角形 triangle，找出一條擁有最小 path sum 路徑，並 return 其值。

    Path 的定義為從 triangle 頂點至底部所形成的路徑
    triangle 為 2D array

"""

#Backtracking
class Solution:

    # @param triangle: List[List[int]]
    # @return int
    def findMinPathSumOfTriangle(self, triangle):
        # Implement me
        output = self.MinPath(triangle,0,0,0)
        return output
    
    def MinPath(self,triangle,row,column,summation):
        if row == len(triangle) - 1:
            return summation + triangle[row][column]
        else:
            left = self.MinPath(triangle,row + 1,column,summation + triangle[row][column])
            right = self.MinPath(triangle,row + 1,column + 1,summation + triangle[row][column])
            if left < right:
                return left
            else:
                return right

triangle = [
      [2],
     [3,4],
    [6,5,7],
   [4,1,8,3]]

s = Solution()
print(s.findMinPathSumOfTriangle(triangle))
