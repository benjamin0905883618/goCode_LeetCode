"""
這道題目曾出現在 DRW 的面試中。

將 input string 根據以下 transition rules 轉態，
直到無法再轉態為止。此 string 只會存在 "A"，"B"，"C" 或 "D" 四種字元。
    Rule 1：若 "A" 和 "B" 相鄰，轉態為 empty string
    Rule 2：若 "C" 和 "D" 相鄰，轉態為 empty string
時間複雜度要求為 O(n)

Example 1:
    Input: "CABADCBD"
    Output: ""
    Explanation: "CABADCBD" -> "CADCBD" -> "CABD" -> "CD" -> ""

Example 2:
    Input: "ACBD"
    Output: "ACBD"
    Explanation: "A" 和 "B" 以及 "C" 和 "D" 均沒有相鄰，無法轉態
"""

#if AB or BA or CD or DC, return True
def check(num1,num2):
    if (num1 == 65 and num2 == 66) or (num1 == 66 and num2 == 65):
        return True
    elif (num1 == 67 and num2 == 68) or (num1 == 68 and num2 == 67):
        return True
    else:
        return False
    
class Solution:

    # @param s: str
    # @return str
    def reduceString(self, s):
        # Implement me
        length = len(s)
        temp_arr =  []
        
        #transfer string to Number
        for i in range(length):
            temp_arr.append(ord(s[i]))
        #print(temp_arr)

        index = 0
        while True:
            #print(temp_arr)
            #print(len(temp_arr))
            #print(index)
            if len(temp_arr) == 0 or index == len(temp_arr) - 1:
                break
            if check(temp_arr[index],temp_arr[index + 1]):
                del temp_arr[index + 1]
                del temp_arr[index]
                index -= 1
            else:
                index += 1

        output_arr = ""

        #transfer number to string
        for i in range(len(temp_arr)):
            output_arr += chr(temp_arr[i])
        return output_arr


s = Solution()
input_string = "CABADCBD"
print(s.reduceString(input_string))

