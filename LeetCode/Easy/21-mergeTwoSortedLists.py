# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answer = []
        # Break once both lists have reached the end
        while l1 is not None or l2 is not None:
            # If l1 has not looked at its last element and added it to the array
            if l1 is not None and l2 is not None:
                if l1.val >= l2.val:
                    answer.append(l2.val)
                    l2 = l2.next
                else:
                    answer.append(l1.val)
                    l1 = l1.next
            elif l1 is None:
                answer.append(l2.val)
                l2 = l2.next
            
            elif l2 is None:
                answer.append(l1.val)
                l1 = l1.next
            
        
        return answer
