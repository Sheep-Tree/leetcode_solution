from tree import *
class Solution:
    node_list = []
    def Convert1(self, pRootOfTree):
        # write code here
        self.travel(pRootOfTree)
        for i in range(len(self.node_list)):
            if i>0:
                self.node_list[i].left = self.node_list[i-1]
            if i<len(self.node_list)-1:
                self.node_list[i].right = self.node_list[i+1]
        return self.node_list[0]


    def travel(self, node):
        if node.left != None:
            self.travel(node.left)
        self.node_list.append(node)
        if node.right != None:
            self.travel(node.right)
if __name__ == '__main__':
    sol = Solution()
    tree_list1 = [5, 3, 8, 2, 4, 6, 9]
    tree_list = [5,4,'#',3,'#',2,'#',1]
    root_node = ConstructTree(tree_list)
    node = sol.Convert1(root_node)
    while node!=None:
        print(node.val)
        node = node.right