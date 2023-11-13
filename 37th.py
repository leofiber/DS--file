def orangesRotting(grid):
    if not grid:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    fresh_oranges = 0
    rotten_oranges = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh_oranges += 1
            elif grid[i][j] == 2:
                rotten_oranges.append((i, j, 0))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0

    while rotten_oranges:
        i, j, minutes = rotten_oranges.pop(0)
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                grid[x][y] = 2
                fresh_oranges -= 1
                rotten_oranges.append((x, y, minutes + 1))

    if fresh_oranges==0:
        return minutes
    else:
        return -1

grid = [[2, 1, 1],[1, 1, 0],[0, 1, 1]]
result = orangesRotting(grid)
print(result)
