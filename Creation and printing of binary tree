class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def create_bt(arr, i, n):
    if i > n:
        return None
    root = TreeNode(arr[i - 1])
    root.left = create_bt(arr, 2 * i, n)
    root.right = create_bt(arr, 2 * i + 1, n)
    return root

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preoder(root):
    if root == None:
        return
    print(root.data)
    preoder(root.left)
    preoder(root.right)

def post(root):
    if root == None:
        return
    post(root.left)
    post(root.right)
    print(root.data)

#Level order 
#leetcode - 102. Binary Tree Level Order Traversal

def levelOrder(root):
    if root == None:
        return []
    ans = []
    queue = [root]
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.data)
        ans.append(level)
    return ans

def findHeight(root):
    if root == None:
        return 0
    l = findHeight(root.left)
    r = findHeight(root.right)
    return 1 + max(l,r)

def zigzagLevelOrder(root):
    if root == None:
        return []
    queue = [root]
    ans = []
    while(queue):
        level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level.append(node.val)
        ans.append(level)
    for i in range(len(ans)):
        if i % 2 == 1:
            ans[i] = ans[i][::-1]
    return ans
