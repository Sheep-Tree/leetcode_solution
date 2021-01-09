class solution:
    def maxValue(self, grid):
        height = len(grid)
        width = len(grid[0])
        dp = [[0 for j in range(width)] for i in range(height)]
        dp[0][0] = grid[0][0]
        for i in range(1,height):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,width):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,height):
            for j in range(1,width):
                dp[i][j] = max(dp[i-1][j] + grid[i][j],dp[i][j-1] + grid[i][j])
        return dp[height-1][width-1]

if __name__ == '__main__':
    sol = solution()
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(sol.maxValue(grid))