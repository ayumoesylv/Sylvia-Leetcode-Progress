class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """            
        visited = set() # contains tuples marking (i, j) coordinates
        
        def bfs(i, j):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            frontier = deque()

            frontier.append((i, j))
            visited.add((i, j))
            while len(frontier) > 0:
                current = frontier.pop()
                for x, y in directions:
                    new_i = current[0] + x
                    new_j = current[1] + y
                    if (0 <= new_i < len(board)) and (0 <= new_j < len(board[0])) and board[new_i][new_j] == 'O' and (not (new_i, new_j) in visited):
                        visited.add((new_i, new_j))
                        frontier.append((new_i, new_j))

        for i in range(len(board)): # i index tracker
            for j in range(len(board[0])): # j index tracker
                if (i == 0) or (j == 0) or (i == (len(board) - 1)) or (j == (len(board[0]) - 1)):
                    if board[i][j] == 'O' and not ((i, j) in visited):
                        bfs(i, j) # mark all connected cells as visited
        for i in range(len(board)): # i index tracker in inner board
            for j in range(len(board[0])): # j index tracker in inner board
                if board[i][j] == 'O' and not (i, j) in visited:
                    board[i][j] = 'X' # change to 'X'

                

        