class Solution:
	def maxProfit(self, prices, fee):
		# 动态规划
		dp = [[None]*2]*len(prices)
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		for i in range(len(prices)):
			dp[i][0] = max(dp[i-1][1]+prices[i]-fee,dp[i-1][0])
			dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
		return dp[len(prices)-1][0]
if __name__ == '__main__':
	mysolution = Solution()
	prices = [4,5,2,4,3,3,1,2,5,4]
	fee = 1
	print(mysolution.maxProfit(prices, fee))

					
