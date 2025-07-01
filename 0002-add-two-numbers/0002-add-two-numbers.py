# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head) -> Optional[ListNode]:
    #     prev = None
    #     while head:
    #         head.next, prev, head = prev, head, head.next
    #     return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1_rev = None
        # ctr1 = 0
        # while l1:
        #     l1.next, l1_rev, l1 = l1_rev, l1, l1.next
        #     ctr1 += 1

        # l2_rev = None
        # ctr2 = 0
        # while l2:
        #     l2.next, l2_rev, l2 = l2_rev, l2, l2.next
        #     ctr2 += 1 

        # l1_c = l1_rev
        # l2_c = l2_rev


        res_list = ListNode()

        head = res_list

        carry = 0
        while l1 or l2 or carry:
            temp = carry
            if l1:
                temp += l1.val
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next

            carry = temp//10
            temp = temp%10
            # res_list.val = temp

            res_list.next = ListNode(temp)
            res_list = res_list.next
        
        return head.next

        

        

        
        

        