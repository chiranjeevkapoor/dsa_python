class Solution:
    def dfs(self, row, col, board, visited):
        visited[row][col] = 1
        m = len(board)
        n = len(board[0])
        directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]
        for drow, dcol in directions:
            nrow = row + drow
            ncol = col + dcol
            if 0<=nrow<m and 0<=ncol<n and visited[nrow][ncol]==0 and board[nrow][ncol]=='O':
                self.dfs(nrow, ncol, board, visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if board[0][j]=='O':
                self.dfs(0, j, board, visited)
            if board[m-1][j]=='O':
                self.dfs(m-1, j, board, visited)
        
        for i in range(m):
            if board[i][0]=='O':
                self.dfs(i, 0, board, visited)
            if board[i][n-1]=='O':
                self.dfs(i, n-1, board, visited)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and visited[i][j] == 0:
                    board[i][j] = 'X'

        