"""
這道題目曾出現在 Microsoft 的面試中。

在某些 Compiler Design 中, 我們會用 Binary Tree 來表示算式, 其中 Leaf Node 為數字, Internal Node 為 Operator, 這樣的 Binary Tree 稱為 Expression Tree. 給定 Expression Tree 的根節點 root, 請實現一個能計算此算式的 function.
    Tree node 的 value 是 string type
    Internal node 包含 "+", "-", "*", "/" 四種可能的 operators

Example 1:
    Input: binary tree = 

        Level 0          "*" (root)
                       /     \
        Level 1      "-"     "/"
                     / \     / \
        Level 2    "5" "6" "3" "2"

    Output: -1.5
    Explanation: 此 binary tree 表達的是 (5 - 6) * (3 / 2) = (-1) * (1.5) = -1.5

Example 2:
    Input: binary tree = 

        Level 0          "*" (root)
                       /     \
        Level 1      "-"     "/"
                     / \     / \
        Level 2    "5" "+" "3" "2"
                       / \
        Level 3     "10" "20"

    Output: -37.5
    Explanation: 此 binary tree 表達的是 (5 - (10 + 20)) * (3 / 2) = (-25) * (1.5) = -37.5
"""
# Definition of a binary tree node
class TreeNode:

    # @param val: str
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # @param root: TreeNode
    # @return float
    def evaluate(self, root):
        # Implement me
        answer = pre_order(root)
        return answer

def pre_order(root):
    if root.left != None:
        left_value = pre_order(root.left)
    if root.right != None:
        right_value = pre_order(root.right)
    if root.val == "-":
        return left_value - right_value
    elif root.val == "+":
        return left_value + right_value
    elif root.val == "*":
        return left_value * right_value
    elif root.val == "/":
        return left_value / right_value
    else:
        return int(root.val)
    

number = input()
root = TreeNode(number)
cursor= root
while True:
    command = input().split(" ")
    if command[0] == "i":
        if command[1] == "l":
            temp = TreeNode(command[2])
            cursor.left = temp
        elif command[1] == "r":
            temp = TreeNode(command[2])
            cursor.right = temp
    elif command[0] == "l":
        cursor = cursor.left
    elif command[0] == "r":
        cursor = cursor.right
    elif command[0] == "b":
        cursor = root
    elif command[0] == "t":
        break
    else:
        print("try again")

s = Solution()
print(s.evaluate(root))
