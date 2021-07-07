"""
這道題目曾出現在 Facebook 的面試中。

給定一個字母排序規則 order，驗證給定的 list of words 是否符合此排序規則 (由小至大排序)。

Constraints:
    所有字母均為小寫字母，即 a 到 z

Example 1:
    Input: words = ["go", "code"], order = "zyxwvutsrqponmlkjihgfedcba"
    Output: True
    Explanation: 根據 order，"g" 小於 "c"，所以此排序是正確的

Example 2:
    Input: words = ["abc", "abz", "bcdefg", "bcde"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: False
    Explanation:
        - "abc" < "abz"，因為 "c" 小於 "z"，符合排序規則
        - "anz" < "bcdefg"，因為 "a" 小於 "b"，符合排序規則
        - "bcdefg" > "bcde"，不符合排序規則，因為若前綴 (prefix) 相同，較長字串的 order 較大
    由於有一項不符合排序規則，因此結果為 False
"""
class Solution:

    # @param words: List[str]
    # @param order: str
    # @return bool
    def verifyWordOrdering(self, words, order):
        # Implement me
        #print(order[0])
        if order[0] == 'a':
            sort_word = sorted(words)
            #print(sort_word)
            if words == sort_word:
                return True
            else:
                return False
        elif order[0] == 'z':
            sort_word = sorted(words,reverse = True)
            #print(sort_word)
            if words == sort_word:
                return True
            else:
                return False
s = Solution()
words = ["abc", "abz", "bcdefg", "bcde"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s.verifyWordOrdering(words,order))
