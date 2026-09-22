# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # first create a dummy node
        dummy=ListNode()
        tail=dummy
        #the condition
        while list1 and list2:
            if list1.val < list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        return dummy.next
        #doesn't work cause the the list is a linked list
        '''
        merge=list1+list2
        merge.sort()
        return merge
        '''