class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def bfs(i, j) -> int:
            """
            Returns the area of the island starting at i, j
            """
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            frontier = deque()
            counter = 0

            frontier.append((i, j))
            grid[i][j] = 0
            counter += 1
            while len(frontier) > 0:
                cur_i, cur_j = frontier.pop()
                for x, y in directions:
                    new_i, new_j = cur_i + x, cur_j + y
                    if (0 <= new_i < len(grid)) and (0 <= new_j < len(grid[0])) and grid[new_i][new_j] == 1:
                        frontier.append((new_i, new_j))
                        grid[new_i][new_j] = 0 # mark as 0 / water
                        counter += 1 # add to counter 
            return counter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    if area > max_area:
                        max_area = area

        return max_area