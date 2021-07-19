"""
這道題目曾出現在 Facebook 的面試中。

給定一個字串 s 及一個正整數 k，
找出最長的 substring 的長度，此 substring 最多只能包含 k 個不同字母。
Example 1:
    Input: s = "abacd", k = 2
    Output: 3
    Explanation: 最長的 valid substring 為 "aba"，其長度為 3
Example 2:
    Input: s = "zzazzzzzz", k = 1
    Output: 6
    Explanation: 最長的 valid substring 為 "zzzzzz"，其長度為 6
"""

class Solution:

    # @param s: str
    # @param k: int
    # @return int
    def findLongestSubstringWithAtMostKDistinctCharacters(self, s, k):
        # Implement me
        maximum = 0
        cat = []
        temp = 0
        for i in range(len(s)):
            #print(s[i])
            if s[i] not in cat:
                cat.append(s[i])
            if len(cat) > k:
                i -= 1
                if maximum < temp:
                    maximum = temp
                temp = 0
                cat = []
            else:
                temp += 1
            #print(temp)
        if maximum < temp:
            maximum = temp
            
        return maximum
        
            
        

        

string = "abacd"
k = 2
s = Solution()
print(s.findLongestSubstringWithAtMostKDistinctCharacters(string,k))
