class solution:
	def maxSubArray(self,nums):
		s = [nums[0]]*len(nums)
		for i in range(1,len(nums)):
			s[i] = max(nums[i],s[i-1]+nums[i])
		max_s = s[0]
		for is_s in s:
			if is_s > max_s:
				max_s = is_s
		return max_s

if __name__ == '__main__':
	sol = solution()
	nums = [-1]
	print(sol.maxSubArray(nums))