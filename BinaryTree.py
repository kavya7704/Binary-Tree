from typing import Optional, List
from collections import deque

class TreeNode:
    def _init_(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if i < len(level_order) and level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

def rob_tree(node: Optional[TreeNode]) -> (int, int):
    if not node:
        return (0, 0)
    left = rob_tree(node.left)
    right = rob_tree(node.right)
    rob = node.val + left[1] + right[1]
    not_rob = max(left) + max(right)
    return (rob, not_rob)

if _name_ == "_main_":
    input_list = input().strip().split()
    level_order = [int(x) if x != 'None' else None for x in input_list]
    root = build_tree(level_order)
    result = max(rob_tree(root))
    print(result)
