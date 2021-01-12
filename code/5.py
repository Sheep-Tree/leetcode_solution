class solution:
	def longestPalindrome(self,s):	# 超时
		dp = [[False for i in range(len(s))] for j in range(len(s))]
		max_str = ""
		for k in range(1,len(s)+1):
			for i in range(len(s)):
				if i+k<=len(s):
					j = i+k-1
					if i==j:
						dp[i][j] = True
					elif k == 2:
						if s[i]==s[j]:
							dp[i][j] = True
					elif (s[i]==s[j]) and (dp[i+1][j-1]==True):
						dp[i][j] = True
					if dp[i][j]:
						max_str = s[i:j+1]
		return max_str

	def longestPalindrome2(self, s)	# 没超时
		size = len(s)
		if size < 2:
			return s
		dp = [[False for _ in range(size)] for _ in range(size)]
		max_len = 1
		start = 0
		for i in range(size):
			dp[i][i] = True
		for j in range(1, size):
			for i in range(0, j):
				if s[i] == s[j]:
					if j - i < 3:
						dp[i][j] = True
					else:
						dp[i][j] = dp[i + 1][j - 1]
				else:
					dp[i][j] = False
				if dp[i][j]:
					cur_len = j - i + 1
					if cur_len > max_len:
						max_len = cur_len
						start = i
		return s[start:start + max_len]
		

if __name__ == '__main__':
	sol = solution()
	s ="babad"
	max_str = sol.longestPalindrome(s)
	print(max_str)
