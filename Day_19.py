"""這道題目曾出現在 Amazon 的面試中。

給定一個字串 array，將互相為 anagram 的字串分在同一組，最後 return 分組後的結果。
    Anagram 的定義是兩個字串所包含的字母及各字母的數量都是一樣的，只是位置不同
        例如 abc 及 cba 互相為 anagram，而 abc 及 cbc 互相不為 anagram
    最終答案可以用任意順序排列

Example 1:
    Input: ["dog", "ban", "banana", "nba", "ananab", "nnabaa", "god"]
    Output: [["dog", "god"], ["banana", "ananab", "nnabaa"], ["ban", "nba"]]
    Explanation:
    ["dog", "god"] 可分為一組，因為兩字串都各有 1 個 d, 1 個 o, 及 1 個 g
    ["banana", "ananab", "nnabaa"] 及 ["ban", "nba"] 也同理

"""
class Solution:

    # @param strings: List[str]
    # @return List[List[str]]
    def groupAnagrams(self, strings):
        # Implement me
        dict = {}
        for i in strings:
            com = check(i)
            if com in dict:
                dict[com].append(i)
            else:
                dict[com] = [i]
        return dict

def check(string):
    output = []
    for i in range(26):
        output.append(0)
    for j in range(len(string)):
        output[ord(string[j]) - 97] += 1
    output = str(output)
    return output

def print_dict(dic):
    for i in dic:
        print(dic[i])

s = Solution()
string_set = ["dog", "ban", "banana", "nba", "ananab", "nnabaa", "god"]
answer = s.groupAnagrams(string_set)
print_dict(answer)
