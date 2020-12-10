class Solution:
    def matrixScore(self, A):	# ！！！这个题目的核心是：行列变换的顺序对最终结果无影响，因此可以先全部行变换再全部列变换！！！
    	height = len(A)
    	width = len(A[0])
    	# 把每行的第一列全变为1
    	for i in range(height):
    		if A[i][0] == 0:
    			# 翻转此行
    			A[i] = [ 1-x for x in A[i]]

    	# 扫描每列,1多则保留,0多则翻转
    	for j in range(width):
    		count_of_one = 0
    		for i in range(height):
    			if A[i][j] == 1:
    				count_of_one += 1
    		if count_of_one <= int(height/2):
    			# 翻转此列
    			for i in range(height):
    				A[i][j] = 1-A[i][j]
    	# 计算数值
    	sum_all = 0
    	for i in range(height):
    		sum_line = 0
    		for j in range(width):
    			sum_line += (2**(width-j-1))*A[i][j]
    		sum_all += sum_line
    	print(A)
    	return sum_all

if __name__ == '__main__':
	mysolution = Solution()
	A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
	print(mysolution.matrixScore(A))
