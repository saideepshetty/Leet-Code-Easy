'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
Code By Saideep Shetty
 '''

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        return Solution.isMirror(root,root)
    
    def isMirror(t1,t2):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        return(t1.val==t2.val) and Solution.isMirror(t1.right,t2.left) and Solution.isMirror(t1.left,t2.right)
