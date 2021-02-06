# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def ConstructTree(tree_list):
    node_list = [TreeNode(x) for x in tree_list]
    for i in range(1,len(tree_list)):
        father_index = int((i-1)/2)
        if int((i-1)/2+0.5) == int((i-1)/2):
            node_list[father_index].left = node_list[i]
        else:
            node_list[father_index].right = node_list[i]
    return node_list[0]

def PrintTree(root):
    node_list = []
    node_list.append(root)

    while len(node_list)>0:
        print([x.val for x in node_list])
        temp_node_list = []
        for node in node_list:
            if node.left!=None:
                temp_node_list.append(node.left)
            if node.right!=None:
                temp_node_list.append(node.right)
        node_list = temp_node_list

if __name__ == '__main__':
    tree_list = [5, 3, 8, 2, 4, 6, 9]
    root_node = ConstructTree(tree_list)
    PrintTree(root_node)