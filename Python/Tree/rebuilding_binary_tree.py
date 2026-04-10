class TreeNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.item, end=" ")


def solve(pre_l, pre_r, in_l, in_r):
    if pre_l > pre_r:
        return None

    root_val = preorder[pre_l]
    root_index = pos[root_val]

    left_size = root_index - in_l

    left = solve(pre_l + 1, pre_l + left_size, in_l, root_index - 1)
    right = solve(pre_l + left_size + 1, pre_r, root_index + 1, in_r)

    return TreeNode(root_val, left, right)


N = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

pos = {v: i for i, v in enumerate(inorder)}

tree = solve(0, N - 1, 0, N - 1)
tree.postorder()
