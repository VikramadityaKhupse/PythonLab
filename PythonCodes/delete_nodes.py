# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/submissions/1381262930/?envType=daily-question&envId=2024-09-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)  

        while head and head.val in nums_set:
            head = head.next
        
        curr_node = head
        while curr_node and curr_node.next:
            if curr_node.next.val in nums_set:
                curr_node.next = curr_node.next.next  
            else:
                curr_node = curr_node.next  
        
        return head
        