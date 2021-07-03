import sys

class Solution:

    # @param nums: List[int]
    # @return int
    def maxSubarraySum(self, nums):
        # Implement me
        summation = 0
        maximum = -sys.maxsize - 1
        length = len(nums)
        for i in range(length):
            summation += nums[i]
            if nums[i] > summation:
                summation = nums[i]
            if summation > maximum:
                maximum = summation
        return maximum
        
        

s = Solution()
array = [3,-1,3,-1,-5,5,-1,-9]
print(s.maxSubarraySum(array))
