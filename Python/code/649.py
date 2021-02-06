class Solution:
	def predictPartyVictory(self, senate):
		num = len(senate)
		power = [1]*num
		while(True):
			for i in range(len(senate)):
				# 禁人同时判断胜利
				print(power)
				if power[i] == 1:
					if senate[i] == 'D':
						useed = False
						for j in range(i,len(senate)):
							if senate[j] == 'R' and power[j] == 1:
								power[j] = 0
								useed = True
								print('ban num ',j)
								break
						if useed == False:
							for j in range(i):
								if senate[j] == 'R' and power[j] == 1:
									power[j] = 0
									useed = True
									print('ban num(back) ',j)
									break
						if useed == False:	# 无人可禁，表示胜利了
							return 'Dire'
					elif senate[i] == 'R':
						useed = False
						for j in range(i+1,len(senate)):
							if senate[j] == 'D' and power[j] == 1:
								power[j] = 0
								useed = True
								print('ban num ',j)
								break
						if useed == False:
							for j in range(i):
								if senate[j] == 'D' and power[j] == 1:
									power[j] = 0
									useed = True
									print('ban num(back) ',j)
									break
						if useed == False:	# 无人可禁，表示胜利了
							return 'Radiant'

if __name__ == '__main__':
	mysolution = Solution()
	senate = "RD"
	senate1 = "RDD"
	print(mysolution.predictPartyVictory(senate))