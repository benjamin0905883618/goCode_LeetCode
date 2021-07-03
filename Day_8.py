# Definition of a binary tree node
class TreeNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    # @param root: TreeNode
    # @param k: int
    # @return int
    def findKthSmallestInBST(self, root, k):
        # Implement me
        output_array = []
        output_pre_order(root,output_array)
        return output_array[k - 1]

def output_pre_order(root,output_array):
    if root.left != None:
        output_pre_order(root.left,output_array)
    output_array.append(root.val)
    if root.right != None:
        output_pre_order(root.right,output_array)
        
def pre_order(root):
    if root.left != None:
        pre_order(root.left)
    print(root.val,end = " ")
    if root.right != None:
        pre_order(root.right)

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
        pre_order(root)
        print()
        break

s = Solution()
print("output = ",s.findKthSmallestInBST(root,4))

