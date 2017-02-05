# http://www.lintcode.com/en/problem/lowest-common-ancestor/


tree_data =  [3,9,20,'#','#',15,7]
#tree_data = [1]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None




def build_tree():
    if build_tree.data_index >= build_tree.data_length:
        return None
        
    node_value = build_tree.data[build_tree.data_index]
    build_tree.data_index += 1

    if node_value == '#':
        return None

    node = TreeNode(node_value)
    node.left = build_tree()
    node.right = build_tree()

    return node


build_tree.data_index = 0
build_tree.data = tree_data
build_tree.data_length = len(tree_data)

root = build_tree()
print(root)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import copy
class Solution:
    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """ 
    def lowestCommonAncestor(self, root, A, B):
        self.route_a = []
        self.route_b = []
        self.route = []

        self.dfs(root, A, B)

        for x in reversed(self.route_a):
            if x in self.route_b:
                return x
        return None

    def dfs(self, node, A, B):
        if self.route_a and self.route_b:
            return

        if node:
            self.route.append(node)
            if not self.route_a and node.val == A.val:
                self.route_a = copy.copy(self.route)
            if not self.route_b and node.val == B.val:
                self.route_b = copy.copy(self.route)

            self.dfs(node.left, A, B)
            self.dfs(node.right, A, B)
            self.route.pop()



solution = Solution()
result = solution.lowestCommonAncestor(root, TreeNode(15), TreeNode(7))
print(result.val)