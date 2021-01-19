class solution:
	def findMaxFrom(self, strs, m, n):
		dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
		dp[0][0] = 0
		for is_str in strs:
			count0,count1 = self.is_count(is_str)
			for i in range(m,-1,-1):
				for j in range(n,-1,-1):
					if i-count0>=0 and j-count1>=0:
						dp[i][j] = max(dp[i-count0][j-count1] + 1,dp[i][j])
		return dp[m][n]

	def is_count(self,is_str):
		count0 = 0
		count1 = 0
		for c in is_str:
			if c=="0":
				count0+=1
			elif c=="1":
				count1+=1
		return count0,count1

if __name__ == '__main__':
	sol = solution()
	strs = ["10", "0001", "111001", "1", "0"]
	m = 5
	n = 3
	print(sol.findMaxFrom(strs,m,n))