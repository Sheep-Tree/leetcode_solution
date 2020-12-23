class Solution:
	def firstUniqChar(self, s):
		alpha_num_index = {}
		for index in range(len(s)):
			if s[index] not in alpha_num_index.keys():
				alpha_num_index[s[index]] = [1,index]
			else:
				alpha_num_index[s[index]][0] += 1
		index = len(s)
		find = False
		for key,value in alpha_num_index.items():
			if value[0] == 1 and value[1] < index:
				index = value[1]
				find = True
		if len(s) == 0 or find == False:
			index = -1
		return index

if __name__ == '__main__':
	sol = Solution()
	s1 = "loveleetcode"
	s2 = "leetcode"
	s3 = "cc"
	print(sol.firstUniqChar(s3))

