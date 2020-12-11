class Solution:
	def generate(self, numRows):
		tangle_list = [[1],[1,1]]
		for i in range(2,numRows):
			temp_list = []
			temp_list.append(1)
			for j in range(1,i):
				temp_list.append(tangle_list[i-1][j-1]+tangle_list[i-1][j])
			temp_list.append(1)
			tangle_list.append(temp_list)
		return tangle_list

if __name__ == '__main__':
	mysolution = Solution()
	print(mysolution.generate(5))
