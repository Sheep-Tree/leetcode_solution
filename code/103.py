# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        deep = 0
        end = False
        if root==None:
            return []
        lists = [[root.val]]
        node_list = [root]
        while not end:
            end = True
            temp_list = []
            for i in range(len(node_list)):	# 正序遍历
                if node_list[i].left != None:
                    temp_list.append(node_list[i].left)
                    end = False
                if node_list[i].right != None:
                    temp_list.append(node_list[i].right)
                    end = False
            if not end:
                if deep % 2 == 1:
                    lists.append([temp_list[i].val for i in range(len(temp_list))])
                else:
                    lists.append([temp_list[i].val for i in range(len(temp_list)-1,-1,-1)])
            deep += 1
            node_list = temp_list
        return lists

