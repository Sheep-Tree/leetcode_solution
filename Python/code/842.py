class solution:
	def splitIntoFibonacci(self, mystr):
		res = []
		if(backtrack(mystr, res, "")):
			return res
		else:
			return []

def backtrack(is_str, res, debug_str):
	str_len = len(is_str)
	if str_len == 0 and len(res)>=3:
		return True

	for i in range(1,str_len+1):
		x = int(is_str[:i])
		if i >= 2 and is_str[0] == "0":
			break
		if x > 2**31-1:
			break
		if len(res) < 2:
			res.append(x)
			if(backtrack(is_str[i:],res,debug_str+"-")):
				return True
			else:
				del res[-1]
		else: 
			if res[-1]+res[-2]==x:
				res.append(x)
				if backtrack(is_str[i:],res,debug_str+"-"):
					return True
				else:
					del res[-1]
	return False



if __name__ == '__main__':
	mystr = "123456579"
	mystr1 = "11235813"
	mystr2 = "112358130"
	mystr3 = "0123"
	mystr4 = "1101111"
	mystr5 = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
	my_solution = solution()
	print(my_solution.splitIntoFibonacci(mystr5))
	
