class Solution:
    def lemonadeChange(self, bills):
    	my_bill_5 = 0
    	my_bill_10 = 0
    	my_bill_20 = 0
    	success = True
    	for bill in bills:
    		if bill == 5:
    			my_bill_5 += 1
    		elif bill == 10:
    			if my_bill_5 > 0:
    				my_bill_10 += 1
    				my_bill_5 -= 1
    			else:
    				success = False
    				break
    		elif bill == 20:
    			if my_bill_10 >= 1 and my_bill_5 >= 1:
    				my_bill_5 -= 1
    				my_bill_10 -= 1
    				my_bill_20 += 1
    			elif my_bill_5 >= 3:
    				my_bill_5 -= 3
    				my_bill_20 += 1
    			else:
    				success = False
    				break
    	return success

if __name__ == '__main__':
	my_solution = Solution()
	bills = [5,5,5,10,20]
	bills2 = [5,5,10]
	bills3 = [10,10]
	bills4 = [5,5,10,10,20]
	print(my_solution.lemonadeChange(bills4))
