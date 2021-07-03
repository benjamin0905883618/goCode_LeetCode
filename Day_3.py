"""
這道題目曾出現在 Facebook 的面試中。

給定 Binary Tree 的根節點 root, 找出此 Binary Tree 的最大寬度。
    Binary Tree 的寬度定義為: 在某個 tree level 中，最左邊的節點至最右邊的節點的距離
    若中間包含空節點 (null node) 則必須將空節點也納入距離的計算
Constraints:
    節點值均為整數
    最大寬度不會超過 32-bit integer 的可表示範圍

Input: binary tree =

    Level 0         9 (root)
                   / \
    Level 1       8   7
                 /   / \
    Level 2     6   5   4
                     \
    Level 3           3

Output: 4
Explanation: Level 2 的節點為 [6, null, 5, 4]，
其寬度為 4 且是整個 Binary Tree 中最寬的

"""
# Definition of a binary tree node
class TreeNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # @param root: TreeNode
    # @return int
    def widthOfBinaryTree(self, root):
        # Implement me
        time = 0
        max = 0
        while True:
            #calculate every level and pick the biggest one
            result = Node_amount(root,time)
            if result > max:
                max = result
            if result == 0:
                break
            time += 1
        return max

#print by inorder
def inorder(root):
    print(root.val)
    if root.left != None:
        inorder(root.left)
    if root.right != None:
        inorder(root.right)

#calculate the width of one of level in binary tree
def Node_amount(root,level):
        if level == 0:
            return 1
        elif level == 1:
            if root.left == None and root.right == None:
                return 0
            else:
                return 2
        else:
            left = 0
            right = 0
            if root.left != None:
                left = Node_amount(root.left,level - 1)
            if root.right != None:
                right = Node_amount(root.right,level - 1)
            return left + right        

#genTree
number = int(input())
root = TreeNode(number)
cursor = root
while True:
    print("root : ",cursor.val)
    command = input().split(" ")
    if command[0] == "i":
        if command[1] == "l":
            number = int(command[2])
            temp = TreeNode(number)
            cursor.left = temp
        elif command[1] == "r":
            number = int(command[2])
            temp = TreeNode(number)
            cursor.right = temp
    elif command[0] == "l":
        cursor = cursor.left
    elif command[0] == "r":
        cursor = cursor.right
    elif command[0] == "back":
        cursor = root
    elif command[0] == "terminate":
        inorder(root)
        break

        
#call function and validation whether the function is good enough
s = Solution()
print(s.widthOfBinaryTree(root))
#number = Node_amount(root,5)
#print(number)
