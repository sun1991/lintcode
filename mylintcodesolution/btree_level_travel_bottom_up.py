# http://www.lintcode.com/zh-cn/problem/binary-tree-level-order-traversal/


tree_data =  [3,9,20,'#','#',15,7]

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




class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        level = 0
        self.result_dict = {}
        self.dfs(root, level)

        result_list = []
        keys = sorted(self.result_dict.keys())

        for key in keys:
            result_list.append(self.result_dict[key])

        return result_list

        
    def dfs(self, node, level):
        if node:
            self.result_dict.setdefault(level, []).append(node.val)
            level += 1
            self.dfs(node.left, level)
            self.dfs(node.right, level)



solution = Solution()
result_list = solution.levelOrder(root)
print(result_list)