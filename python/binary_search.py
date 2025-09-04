arry = [1, 2, 3, 4, 5, 6, 7, 8]


def binarysearch(arry, target):
    length = len(arry)
    l = 0
    r = length - 1
    while l <= r:
        m = (
            l + ((r - l) // 2)
        )  # do the first to prevent integer overflow when l and r are large  m = (l + r) // 2
        if arry[m] == target:
            return m
        if arry[m] < target:
            l = m + 1
        else:
            r = m - 1
    return False


# print(f"found target at {binarysearch(arry, 7)}")
class node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)


a = node(1)
b = node(2)
c = node(3)
d = node(4)
e = node(5)
f = node(10)

"""
        1 
     2    3
  4   5  10
"""
a.left, a.right = b, c
b.left, b.right = d, e
c.left = f


def dfs(node: node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def bfs(node: node):
    from collections import deque

    q = deque()
    q.append(node)
    while q:
        # print(q)
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# print(f"dfs {dfs(a)}\n\n")
print(f"bfs {bfs(a)}\n\n")
