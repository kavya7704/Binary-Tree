from collections import deque

def construct(nums):
    if not nums: return None
    m, i = max(nums), nums.index(max(nums))
    return [m, construct(nums[:i]), construct(nums[i+1:])]

def toList(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node[0])
            q.extend([node[1], node[2]])
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res

nums = list(map(int, input().split()))
print(toList(construct(nums)))
