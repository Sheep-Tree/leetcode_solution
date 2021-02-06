class Solution:
	def wordPattern(self, pattern, s):
		s_list = s.split(' ')
		if len(pattern)!=len(s_list):
			return False
		pattern_dic = {}
		s_pattern = []
		for i in range(len(pattern)):
			if pattern[i] not in pattern_dic.keys():
				if s_list[i] in s_pattern:
					return False
				print("add {} to dic,key={}".format(pattern[i],s_list[i]))
				pattern_dic[pattern[i]] = s_list[i]
				s_pattern.append(s_list[i])
			elif pattern_dic[pattern[i]] != s_list[i]:
				return False
		return True

if __name__ == '__main__':
	mysolution = Solution()
	pattern = "abba"
	s = "dog dog dog dog"

	print(mysolution.wordPattern(pattern,s))

