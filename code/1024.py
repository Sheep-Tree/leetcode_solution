class solution:
	def videoStitching(self, clips, T):
		dp = [-1]*T
		last_end = 0
		for i in range(T):
			if i<=last_end:
				dp[i] = dp[i-1]
			else:
				for clip in clips:
					if clip[1]>last_end and clip[0]<=last_end:
						dp[i] = dp[i-1]+1