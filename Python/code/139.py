class solution:
	def wordBreak(self, s, wordDict):
		dp = [False]*len(s)
		max_word_len = 0
		for word in wordDict:
			if len(word) > max_word_len:
				max_word_len = len(word)
		for i in range(len(s)):
			for j in range(1,max_word_len+1):
				print(i,j,s[:i+1],s[i-j+1:i+1])
				if s[:i+1] in wordDict:
					dp[i] = True
				if i-j<0:
					break
				if dp[i-j] and (s[i-j+1:i+1] in wordDict):
					dp[i] = True
		return dp[len(s)-1]

if __name__ == '__main__':
	sol = solution()
	s = "a"
	wordDict = ["a"]
	print(sol.wordBreak(s,wordDict))