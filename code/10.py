class solution:
	s = ""
	p = ""
	def isMatch(self,s,p):
		dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
		dp[0][0] = True
		self.s = s
		self.p = p
		for i in range(len(s)+1):
			for j in range(1,len(p)+1):
				if p[j-1]=="*":
					if not self.match(i,j-1):
						dp[i][j] = dp[i][j-2]
						print("1.",i,j,dp[i][j])
					else:
						dp[i][j] = dp[i][j-2] | dp[i-1][j]
						print("2.",i,j,dp[i][j])
				elif self.match(i,j):
					dp[i][j] = dp[i-1][j-1]
					print("3.",i,j,dp[i][j])
		return dp[len(s)][len(p)]

	def match(self,s_index,p_index):
		if s_index == 0:
			return False
		elif self.p[p_index-1]=="." or self.s[s_index-1]==self.p[p_index-1]:
			return True
		else:
			return False

if __name__ == '__main__':
	sol = solution()
	s = "aa"
	p = "a*"
	print(sol.isMatch(s,p))