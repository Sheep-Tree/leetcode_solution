class Solution:
	def wiggleMaxLength(self, nums):
		# 贪心算法，删掉不在峰值上的元素就可以了
		peak_num = 0
		last_up = None	# 递增还是递减
		now_up = None
		for i in range(len(nums)):
			if i == len(nums)-1:
				peak_num += 1
				break
			if nums[i+1]>nums[i]:
				now_up = True
			elif nums[i+1]<nums[i]:
				now_up = False
			if last_up != now_up:
				peak_num += 1
			last_up = now_up
		return peak_num

if __name__ == '__main__':
	my_solution = Solution()
	nums1 = [1,7,4,9,2,5]
	nums2 = [1,17,5,10,13,15,10,5,16,8]
	nums3 = [1,2,3,4,5,6,7,8,9]
	nums4 = [0,0,0]
	nums5 = [0,0]
	nums6 = [0]
	print(my_solution.wiggleMaxLength(nums4))
		
