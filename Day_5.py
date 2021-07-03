"""
這道題目曾出現在 Uber 的面試中。

給定一個 linked list 的 head node, 刪除所有總和為 0 的 sub linked lists,
直到此 linked list 不存在一個總和為 0 的 sub linked list 為止,
最後 return 刪除後的 linked list head node。

Example 1:
    Input: 3 -> 2 -> 1 -> -1 -> -2 -> None
    Output: 3 -> None
    Explanation: Sub list 2 -> 1 -> -1 -> -2 的總和為 0, 所以可把此 sub list 刪除

Example 2:
    Input: -5 -> 2 -> 1 -> -3 -> 10 -> 1 -> 2 -> -2 -> None
    Output -5 -> 10 -> 1 -> None
    Explanation: Sub lists 2 -> 1 -> -3 及 2 -> -2 各自的總和為 0, 所以可把這兩個 sub lists 刪除
"""

# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @retrun ListNode
    def removeZeroSumSublists(self, head):
        # Implement me
        new_head = ListNode(0)
        temp_head = new_head
        cursor = head
        while True:
            cursor_1 = cursor
            sum = 0
            #if sum == 0 then stop loop and delete the sublist
            while True:
                #print(cursor_1.val)
                sum += cursor_1.val
                if sum == 0:
                    break
                if cursor_1.next.val != None:
                    cursor_1 = cursor_1.next
                else:
                    break
            #delete the sublist or merge the sublist
            if sum == 0:
                if cursor_1.next.val == None:
                    temp_head.next = ListNode(None)
                    break
                else:
                    cursor = cursor_1.next
            else:
                temp_head.next = cursor
                temp_head = temp_head.next
                if temp_head.val == None:
                    break
                cursor = cursor.next
        return new_head.next
                
#outpu list
def print_List(root):
    cursor = root
    while True:
        print(cursor.val,end = " ")
        if cursor.next != None:
            cursor = cursor.next
        else:
            break

#input
input = input().split(">")
if input[0] == None:
    print(None)
else:
    root = ListNode(int(input[0]))
    cursor = root
    for i in range(1,len(input)):
        if input[i] == "None":
            temp = ListNode(None)
            cursor.next = temp
            break
        temp = ListNode(int(input[i]))
        cursor.next = temp
        cursor = cursor.next
    #print_List(root)
    #print()

    #call function and validation whether it is good enough
    s = Solution()
    new_List = s.removeZeroSumSublists(root)
    print_List(new_List)
    print()
