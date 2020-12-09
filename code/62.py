class Solution:
	road_num = 0
	def uniquePath(self, m, n):
		return self.uniquePath_iter(m, n)

	# 递归解法（超时）
	def uniquePath_recu(self, m, n):
		if m == 1 and n == 1:
			self.road_num += 1
			return
		elif m == 1 and n == 2:
			# 向右走一步就到终点了
			self.road_num += 1
			return
		elif n == 1 and m == 2:
			# 向下走一步就到终点了
			self.road_num += 1
			return
		elif n>=1 and m>=1:
			# 向右走
			self.uniquePath_recu(m-1,n)
			# 向左走
			self.uniquePath_recu(m,n-1)

	# 动态规划解法
	def uniquePath_iter(self, m, n):
		dp = [[0 for j in range(n)] for i in range(m)]
		for i in range(m):
			dp[i][0] = 1
		for j in range(n):
			dp[0][j] = 1
		#print(dp)
		for i in range(1,m):
			for j in range (1,n):
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
				#print(dp)
		return dp[m-1][n-1]



if __name__ == '__main__':
	my_solution = Solution()
	print(my_solution.uniquePath(3,7))