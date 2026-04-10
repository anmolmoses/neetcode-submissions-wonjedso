class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque()

        def addGrid(row, col):
            if row < 0 or row == ROW or col < 0 or col == COL or (row, col) in visited or grid[row][col] == -1:
                return
            queue.append([row, col])
            visited.add((row, col))
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))
        
        dist = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = dist
                addGrid(row + 1, col)
                addGrid(row, col + 1)
                addGrid(row - 1, col)
                addGrid(row, col - 1)
            dist += 1
        