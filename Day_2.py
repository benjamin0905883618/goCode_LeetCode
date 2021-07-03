"""
這道題目曾出現在 Facebook 的面試中。

給定一個 linked list 的 head node，將指定區間內的節點反轉，並 return 新 linked list 的 head node。
    指定區間之定義為: 第 m 個 node 到第 n 個 node 所形成的 linked list
    Time complexity 要求: One-pass O(N)
Constraints:
    m and n are positive integers
    1 <= m < n <= length of the linked list

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 4
Output: 6 -> 3 -> 4 -> 5 -> 2 -> 1
Explanation: 將第二個 node 到第四個 node 所形成的 Linked List 反轉

Input: Linked List = 6 -> 5 -> 4 -> 3 -> 2 -> 1, m = 2, n = 6
Output: 6 -> 1 -> 2 -> 3 -> 4 -> 5
Explanation: 將第二個 node 到第六個 node 所形成的 Linked List 反轉

"""
# Definition of a linked list node
class ListNode:

    # @param val: int
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    # @param head: ListNode
    # @param m: int
    # @param n: int
    # @return ListNode
    def reverseBetween(self, head, m, n):
        # Implement me

        #Initial some value
        temp_array = []
        new_Head = ListNode(0)
        index = 1
        flag = 0
        cursor = head
        new_cursor = new_Head

        # if n equal to m,we don;t need to do anything,
        #just return the original head
        if n == m:
            return head
        #if n ont equal to m
        else:
            while True:
                #print(cursor.val)
                #if index between n & m, we need to store the value
                if index >= m and index <= n:
                    #print("between")
                    flag = 1
                    temp_array.append(cursor.val)
                #if index > n and the reverse array haven't insert
                #Don't forget to insert the original insertion 
                elif index > n and flag == 1:
                    #print("over,but haven't insert")
                    flag = 0
                    length = len(temp_array) - 1
                    for i in range(length,-1,-1):
                        temp = ListNode(temp_array[i])
                        new_cursor.next = temp
                        new_cursor = new_cursor.next
                    temp = ListNode(cursor.val)
                    new_cursor.next = temp
                    new_cursor = new_cursor.next
                #if index lower than m ,or we have inserted the reverse array
                else:
                    #print("lower or over")
                    temp = ListNode(cursor.val)
                    new_cursor.next = temp
                    new_cursor = new_cursor.next
                
                #if we pass through the original list
                if cursor.next != None:
                    index += 1
                    cursor = cursor.next
                else:
                    break
            #if reverse range equal to the end of original length,
            #we need to insert reverse sentence to new_Head
            if index == n and flag == 1:
                    #print("over,but haven't insert")
                    flag = 0
                    length = len(temp_array) - 1
                    for i in range(length,-1,-1):
                        temp = ListNode(temp_array[i])
                        new_cursor.next = temp
                        new_cursor = new_cursor.next
            return new_Head.next

def print_List(head):
    cursor = head
    while True:
        if cursor.next == None:
            print(cursor.val)
            break
        else:
            print(cursor.val,end = " ")
            cursor = cursor.next
            continue

#test answer

#initial test list
head = ListNode(6)
cursor = head
for i in range(5,0,-1):
    temp = ListNode(i)
    cursor.next = temp
    cursor = cursor.next

print("Input : ")
#Check that if test list be generated just like we think 
print_List(head)
#Call class and use the function
s = Solution()
new_Head = s.reverseBetween(head,2,6)

print("Output : ")
#Check if the answer is correct
print_List(new_Head)
                
        
