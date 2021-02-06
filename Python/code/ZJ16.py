# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        x1 = p1.val
        x2 = p2.val
        p = ListNode(0)
        while p1!=None or p2!=None:
            if p1!=None and p2!=None:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            elif p1==None:
                p.next = p2
                p2 = p2.next
            elif p2==None:
                p.next = p1
                p1 = p1.next
            p = p.next
        return p.next
