# http://www.lintcode.com/en/problem/binary-tree-serialization/

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
    def serialize(self, root):
        self.value_list = []
        self.dfs(root)
        ss = ''
        for item in self.value_list:
            ss += str(item) + ','

        return ss


    def dfs(self, node):
        if node:
            self.value_list.append(node.val)
            self.dfs(node.left)
            self.dfs(node.right)
        else:
            self.value_list.append('#')

    def deserialize(self, data):
        if not data:
            return None

        value_list = self.loads(data)
        self.data_index = 0
        self.data = value_list
        self.data_length = len(value_list)

        return self.build_tree()

    def loads(self, data):
        str_list = data.split(',')
        value_list = [int(item) if item != '#' else item for item in str_list if item]
        return value_list


    def build_tree(self):
        if self.data_index >= self.data_length:
            return None

        node_value = self.data[self.data_index]
        self.data_index += 1

        if node_value == '#':
            return None

        node = TreeNode(node_value)
        node.left = self.build_tree()
        node.right = self.build_tree()

        return node

solution = Solution()
result = solution.serialize(root)
solution.deserialize(result)

