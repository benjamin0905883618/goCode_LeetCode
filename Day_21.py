"""
這道題目曾出現在 Facebook 的面試中。

給定一個 sorted integer array nums，將 nums 中的連續數字以區間表示，最後 return 這些區間。
    nums 中可能出現重複的數
"""
class Solution:

    # @param nums: List[int]
    # @return List[str]
    def convertNumbersToRanges(self, nums):
        # Implement me
        dict = {}
        i = 0
        temp = 0
        while True:
            if i == len(nums):
                break
            #print("*",nums[i])
            dict[nums[i]] = nums[i]
            temp = nums[i]
            i += 1
            while True:
                if i == len(nums):
                    break
                elif nums[i] == dict[temp] + 1:
                    #print("+",nums[i])
                    dict[temp] = nums[i]
                    i += 1
                else:
                    break
                    
        array = []
        for i in dict:
            if i == dict[i]:
                array.append(str(i))
            else:
                array.append(str(i) + "->" + str(dict[i]))
        return array


nums = []
s = Solution()
print(s.convertNumbersToRanges(nums))
