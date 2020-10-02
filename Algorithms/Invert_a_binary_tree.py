'''
INPUT:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

EXPECTED OUTPUT:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Solution
class Solution(object):
	def invertTree(self, root):
		'''
		:typeRoot: TreeNode
		:rType: TreeNode
		'''
		if root == None:
			return root
		tmp = root.left
		root.left = self.invertTree(root.right)
		root.right = self.invertTree(tmp)
		return root
