import sys

class Solution:

    # @param nums: List[int]
    # @return int
    def maxSubarraySum(self, nums):
        # Implement me
        summation = 0
        maximum = -sys.maxsize - 1
        length = len(nums)
        max_length_arr = []
        temp_arr = []
        for i in range(length):
            summation += nums[i]
            temp_arr += [nums[i]]
            #print(max_length_arr)
            #print(summation)
            if nums[i] > summation:
                summation = nums[i]
                temp_arr = [nums[i]]
            if summation > maximum:
                maximum = summation
                max_length_arr = []
                max_length_arr += temp_arr
                #print(max_length_arr)
            elif summation == maximum:
                if len(temp_arr) > len(max_length_arr):
                    max_length_arr = []
                    max_length_arr += temp_arr
                    #print(max_length_arr)
        return max_length_arr
        
        

s = Solution()
array = [-200,100,-100,200,-200,200,-300]
print(s.maxSubarraySum(array))
