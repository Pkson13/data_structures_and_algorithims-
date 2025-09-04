from collections import deque

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    visited = set()

    def bfs(grid, r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))
        while q:
            r, c = q.popleft()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    row in range(rows)
                    and col in range(colums)
                    and grid[row][col] == "1"
                    and (row, col) not in visited
                ):
                    q.append((row, col))
                    visited.add((row, col))

    rows, colums = len(grid), len(grid[0])
    res = 0

    for r in range(rows):
        for c in range(colums):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(grid, r, c)
                res += 1
    return res


print(numIslands(grid))
