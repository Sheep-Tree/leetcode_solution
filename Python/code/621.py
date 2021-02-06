class Solution:
	def leastInterval(self, tasks, n):
		task_dic = {}
		max_task = None
		for i in range(len(tasks)):
			if tasks[i] not in task_dic:
				task_dic[tasks[i]] = 1
				if len(task_dic) == 1:
					max_task = tasks[i]
			else:
				task_dic[tasks[i]] += 1
				if task_dic[tasks[i]] > task_dic[max_task]:
					max_task = tasks[i]
		list_box = [[max_task]+[None]*n]*task_dic[max_task]
		extra = 1
		for key,value in task_dic.items():
			if key != max_task and value == task_dic[max_task]:
				extra += 1
		time1 = (n+1)*(task_dic[max_task]-1) + extra
		time2 = len(tasks)
		return time1 if time1 > time2 else time2

if __name__ == '__main__':
	mmysolution = Solution()
	tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
	n = 2
	print(mmysolution.leastInterval(tasks,n))

