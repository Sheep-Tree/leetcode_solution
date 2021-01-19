class solution:
	def findBall(self,grid):
		col = len(grid[0])
		row = len(grid)
		print(col,row)
		dp = [[-1 for _ in range(col)] for _ in range(row+1)]
		for l in range(row+1):
			for i in range(col):
				if l == 0:
					dp[l][i] = i
				else:
					if dp[l-1][i] == -1:
						dp[l][i] = -1
					else:
						#print("grid:",grid[:][l-1])
						if grid[l-1][dp[l-1][i]]==1 and dp[l-1][i]!=col-1 and grid[l-1][dp[l-1][i]+1]==1:
							#print("grid[{}][{}]={},dp[l-1][i]={},grid[{}][{}]={}"
							#.format(dp[l-1][i],l-1,grid[dp[l-1][i]][l-1],dp[l-1][i],dp[l-1][i]+1,l-1,grid[dp[l-1][i]+1][l-1]))
							dp[l][i] = dp[l-1][i] + 1
							#print("{}->{}".format(dp[l-1][i],dp[l][i]))
						elif grid[l-1][dp[l-1][i]]==-1 and dp[l-1][i]!=0 and grid[l-1][dp[l-1][i]-1]==-1:
							#print("grid[dp[l-1][i]][l-1]={},dp[l-1][i]={},grid[dp[l-1][i]-1][l-1]={}"
							#	.format(grid[dp[l-1][i]][l-1],dp[l-1][i],grid[dp[l-1][i]-1][l-1]))
							dp[l][i] = dp[l-1][i] - 1
							#print("{}->{}".format(dp[l-1][i],dp[l][i]))
						else:
							dp[l][i] = -1
							#print("{}->{}".format(dp[l-1][i],dp[l][i]))
			print(dp[l][:])
		return dp[-1][:]

if __name__ == '__main__':
	sol = solution()
	grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
	grid2 = [[-1]]
	grid3 = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
	print("result:",sol.findBall(grid3))


