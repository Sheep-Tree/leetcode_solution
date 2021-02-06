class solution:
	def maxProfile(self, prices):
		buy1 = [0]*len(prices)
		buy1[0] = -1*prices[0]
		sell1 = [0]*len(prices)
		buy2 = [0]*len(prices)
		buy2[0] = -1*prices[0]
		sell2 = [0]*len(prices)
		for i in range(len(prices)):
			if i>0:
				buy1[i] = max(buy1[i-1],0-prices[i])
				sell1[i] = max(sell1[i-1],buy1[i-1]+prices[i])
				buy2[i] = max(buy2[i-1],sell1[i-1]-prices[i])
				sell2[i] = max(sell2[i-1],buy2[i-1]+prices[i])
		return sell2[len(prices)-1]

if __name__ == '__main__':
	sol = solution()
	prices = [1]
	print(sol.maxProfile(prices))

		