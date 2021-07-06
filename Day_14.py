"""
這道題目曾出現在 Amazon 的面試中。

將給定的字串進行切割，目標是切出最多段 substring，切割的條件為 "每一種 character 僅能出現在一個 substring 內"，最後 return 切割後各 substring 的長度。
    若 input 字串為空，則 return 一個空的 array
    時間複雜度要求為 O(n)
Constraints:
    所有 character 都是英文小寫字母，即 a 到 z

Example 1:
    Input: "ababcbacadefegdehijhklij"
    Output: [9, 7, 8]
    Explanation:
    此字串可以被切割成三段 substring，分別為 "ababcbaca" (長度 9)，
    "defegde" (長度 7)，及 "hijhklij" (長度 8)
        - "a", "b", "c" 僅存在於第 1 個 substring
        - "d", "e", "f", "g" 僅存在於第 2 個 substring
        - "h", "i", "j", "k", "l" 僅存在於第 3 個 substring
    Note: 根據切割條件，也可以切成 "ababcbacadefegde" 及 "hijhklij"，
    但是這樣只有兩段，題目的要求是切成最多段
"""
class Solution:

    # @param s: str
    # @return List[int]
    def partitionString(self, s):
        # Implement me

        #find interval for every alphabet
        dict = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]][1] = i
                #print(s[i],dict[s[i]])
            else:
                dict[s[i]] = [i,i]
                #print(s[i],dict[s[i]])

        #check every interval
        #for i in dict:
            #print(dict[i])
        
        #solve the region that overlapping
        list = []
        max_interval = -1
        for i in dict:
            if dict[i][0] > max_interval:
                list.append(dict[i][1])
                max_interval = dict[i][1]
            if dict[i][0] < max_interval and dict[i][1] > max_interval:
                max_interval = dict[i][1]
                list[-1] = dict[i][1]
        #transform index from 0 to 1
        for i in range(len(list) - 1,0,-1):
            list[i] = list[i] - list[i - 1]
        list[0] = list[0] + 1
        return list

s = Solution()
string = "ababcbacadefegdehijhklij"
print(s.partitionString(string))
