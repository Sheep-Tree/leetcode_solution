class Solution:
	n_str = ""
	r_list = []
	def monitineIncreasingDigits(self, N):
		self.n_str = str(N)
		self.r_list = len(self.n_str)*[0]
		self.backtrack(0)
		# self.r_list = [int(self.n_str[0])-1] + (len(self.n_str)-1)*[9]
		result = 0
		for i in range(len(self.r_list)):
			result += self.r_list[i]*(10**(len(self.r_list)-i-1))
		return result

	def timeout(self, N):
		for i in range(N,0,-1):
			num_str = str(i)
			last_num = 0
			flag = True
			for num in num_str:
				if int(num) >= last_num:
					last_num = int(num)
				else:
					flag = False
					break
			if flag == True:
				return i
		return "error!"

	def backtrack(self, deep):
		print("-"*deep,"now_list:{},deep:{}".format(self.r_list,deep))
		if deep == len(self.n_str):
			# 找到了
			return True
		max_n = int(self.n_str[deep])
		if deep == 0:
			min_n = 0
		else:
			min_n = int(self.n_str[deep-1])
		print("-"*deep,"min_n:{},max_n:{}".format(min_n,max_n))
		if (min_n>max_n):
			return False
		for j in range(max_n,min_n-1,-1):
			self.r_list[deep] = j
			if j < max_n:
				self.r_list[deep+1:] = [9]*(len(self.r_list)-deep-1)
				return True
			if self.backtrack(deep+1):
				return True

		return False

if __name__ == '__main__':
	my_solution = Solution()
	N1 = 10
	N2 = 1234
	N3 = 332
	N4 = 963856657
	N5 = 120
	print(my_solution.monitineIncreasingDigits(N1))
