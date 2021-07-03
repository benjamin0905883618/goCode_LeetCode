"""
這道題目曾出現在 Amazon 的面試中。

將 k 個排序過的 linked list merge 成一個新的已排序的 linked list, 並 return merge 後的 linked list head node。Input 是長度為 k 的 array, 該 array 存放 k 個 linked list 的 head node。
    時間複雜度要求為 O(nlogk), 其中 n 為 merge 後的 linked list 總長度
Constraints:
    k >= 0
Example 1:
    Input: lists = [5 -> 10, 1 -> 3 -> 5 -> 7, -1 -> 11, 0 -> 10 -> 20]
    Output: -1 -> 0 -> 1 -> 3 -> 5 -> 5 -> 7 -> 10 -> 10 -> 11 -> 20

Example 2:
    Input: lists = [-5, -10 -> 100, 9, None]
    Output: -10 -> -5 -> 9 -> 100

"""
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param lists: List[ListNode]
    # @return ListNode
    def mergeKSortedLists(self, lists):
        # Implement me
        new_list = []
        length = len(lists)
        """
        for i in range(length):
            print_List(lists[i])
            print()
        print()
        """
        #if there is only one list inside array
        #we don't need to do anything
        if length == 1:
            return lists
        for i in range(0,length,2):
            #print(i)
            #print(length)
            #we need to check if lists[i + 1] exist,
            #if doesn't,just put lists[i] into the new list set
            if lists[i + 1]:
                cursor_1 = lists[i]
                cursor_2 = lists[i + 1]
                new_head = ListNode(0)
                cursor = new_head
                while True:
                    #print("insert : ",cursor_1.val)
                    #print("insert : ",cursor_2.val)

                    #check if value is empty,
                    #this step shouldn't be merge with other "if"
                    #because "or" will check empty first,then check "<" after
                    if cursor_2.val == None:
                        temp = ListNode(cursor_1.val)
                        cursor.next = temp
                        cursor = cursor.next
                        if cursor_1.next == None:
                            cursor_1.val = None
                        else:
                            cursor_1 = cursor_1.next
                    elif cursor_1.val == None:
                        temp = ListNode(cursor_2.val)
                        cursor.next = temp
                        cursor = cursor.next
                        if cursor_2.next == None:
                            cursor_2.val = None
                        else:
                            cursor_2 = cursor_2.next
                    #pick the smaller one
                    elif int(cursor_1.val) < int(cursor_2.val):
                        temp = ListNode(cursor_1.val)
                        cursor.next = temp
                        cursor = cursor.next
                        if cursor_1.next == None:
                            cursor_1.val = None
                        else:
                            cursor_1 = cursor_1.next
                    elif int(cursor_1.val) >= int(cursor_2.val):
                        temp = ListNode(cursor_2.val)
                        cursor.next = temp
                        cursor = cursor.next
                        if cursor_2.next == None:
                            cursor_2.val = None
                        else:
                            cursor_2 = cursor_2.next
                    
                    if cursor_1.val == None and cursor_2.val == None:
                        break
                new_list.append(new_head.next)
            else:
                new_list.append(list[i])
                continue
            #print_List(new_head)
            #new_list.append(new_head)

        #you need to add self inorder to recur the function
        return self.mergeKSortedLists(new_list)

#outpu the linkelist
def print_List(root):
    while True:
        print(root.val,end = " ")
        if root.next != None:
            root = root.next
        else:
            break

#input the un-sort list set
command = input().split(",")
length = len(command)
list = []
for i in range(length):
    number = command[i].split(">")
    width = len(number)
    if number[0] == "None":
        head = ListNode(None)
    else:
        head = ListNode(number[0])
    cursor = head
    for j in range(1,width):
        if number[j] == None:
            temp = ListNode(None)
        else:
            temp = ListNode(number[j])
        cursor.next = temp
        cursor = cursor.next
    list.append(head)
"""
list_length = len(list)
for i in range(list_length):
    print_List(list[i])
    print()
"""

#call function and validation whether the function is good enough
s = Solution()
output = s.mergeKSortedLists(list)
print_List(output[0])
