"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

"""
#Solution

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent = {root.val : 0}
        label = {root.val : 1}
        
        def setParent(root, l):
            if not root:
                returns
            if root.left:
                parent[root.left.val] = root.val
                label[root.left.val] = l + 1
                setParent(root.left, l + 1)
            if root.right:
                parent[root.right.val] = root.val
                label[root.right.val] = l + 1
                setParent(root.right, l + 1)
                
        setParent(root, 1)
        return parent[x] != parent[y] and label[x] == label[y]