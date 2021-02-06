# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        list_1 = []
        if listNode == None:
            return []
        is_node = listNode
        while is_node.next != None:
            list_1.append(listNode.val)
            is_node = is_node.next
        print(list_1)
        return [list_1[i] for i in range(len(list_1)-1,-1,-1)]

if __name__ == '__main__':
    sol = Solution()