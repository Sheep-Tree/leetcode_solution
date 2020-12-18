class Solution:
	def findTheDifference(self, s, t):
		s_dic = {}
		t_dic = {}
		for c in s:
			if c in s_dic:
				s_dic[c] += 1
			else:
				s_dic[c] = 1
		for c in t:
			if c in t_dic:
				t_dic[c] += 1
			else:
				t_dic[c] = 1
		for key,value in t_dic.items():
			if (key not in s_dic) or (s_dic[key] != value):
				return key
		return None

if __name__ == '__main__':
	mysole = Solution()
	s = "abcd"
	t = "abcde"
	print(mysole.findTheDifference(s,t))
