# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        root_node = TreeNode(pre[0])
        if len(pre)>1:
            for i in range(len(tin)):
                if tin[i] == root_node.val:
                    root_node.left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])
                    root_node.right = self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
        return root_node

if __name__ == '__main__':
    sol = Solution()
    pre = [1,2,4,3,5,6]
    tin = [4,2,1,5,3,6]
    sol.reConstructBinaryTree(pre,tin)