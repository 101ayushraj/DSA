# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        main_head=head
        curr=head
        joint=head
        cnt=1
        while cnt<left:
            joint=curr
            curr=curr.next
            cnt+=1

        future_tail=curr
        prev=None

        while cnt<=right:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            cnt+=1

        if left > 1:
            joint.next = prev

        future_tail.next=curr
        if left>1:
            return main_head
        return prev