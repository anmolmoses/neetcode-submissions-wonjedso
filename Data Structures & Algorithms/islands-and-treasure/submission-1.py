class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        queue = collections.deque()
        visited = set()

        def addRow(row, col):
            if row < 0 or row == ROW or col < 0 or col == COL or (row, col) in visited or grid[row][col] == -1:
                return
            queue.append([row, col])
            visited.add((row, col))
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0:
                    queue.append([row, col])
                    visited.add((row, col))
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = distance
                addRow(row + 1, col)
                addRow(row, col + 1)
                addRow(row - 1, col)
                addRow(row, col - 1)
            distance += 1

        