class Solution:
	def candy(self, ratings):	# 实际也是贪心
		candy_list = [1]*len(ratings)
		if len(ratings) == 1:
			return 1
		if len(ratings) == 0:
			return 0
		for i in range(1,len(ratings)):
			if ratings[i] > ratings[i-1] and candy_list[i]<=candy_list[i-1]:
				candy_list[i] = candy_list[i-1] + 1
			print(candy_list)
		print("------")
		for i in range(len(ratings)-2,-1,-1):
			if ratings[i] > ratings[i+1] and candy_list[i]<=candy_list[i+1]:
				candy_list[i] = candy_list[i+1] + 1
			print(candy_list)
		all_candy = 0
		for candy in candy_list:
			all_candy += candy
		return all_candy
				
	def candy_old(self, ratings):	# 这个提交超时了
		candy_list = [1]*len(ratings)
		change = True
		if len(ratings) == 1:
			return 1
		if len(ratings) == 0:
			return 0
		while change:
			change = False
			for i in range(len(ratings)):
				if i == 0:
					if ratings[i] > ratings[i+1] and candy_list[i]<=candy_list[i+1]:
						candy_list[i] += 1
						change = True
					elif ratings[i] < ratings[i+1] and candy_list[i]>=candy_list[i+1]:
						candy_list[i+1] += 1
						change = True
				elif i == len(ratings)-1:
					if ratings[i] > ratings[i-1] and candy_list[i]<=candy_list[i-1]:
						candy_list[i] += 1
						change = True
					elif ratings[i] < ratings[i-1] and candy_list[i]>=candy_list[i-1]:
						candy_list[i-1] += 1
						change = True
				else:
					if ratings[i] > ratings[i+1] and candy_list[i]<=candy_list[i+1]:
						candy_list[i] += 1
						change = True
					elif ratings[i] < ratings[i+1] and candy_list[i]>=candy_list[i+1]:
						candy_list[i+1] += 1
						change = True
					if ratings[i] > ratings[i-1] and candy_list[i]<=candy_list[i-1]:
						candy_list[i] += 1
						change = True
					elif ratings[i] < ratings[i-1] and candy_list[i]>=candy_list[i-1]:
						candy_list[i-1] += 1
						change = True
		all_candy = 0
		for candy in candy_list:
			all_candy += candy
		return all_candy

if __name__ == '__main__':
	mysol = Solution()
	ratings = [0]
	ratings1 = [1,0,2]
	ratings2 = [1,2,2]
	ratings3 = [1,2,87,87,87,2,1]
	print(mysol.candy(ratings1))