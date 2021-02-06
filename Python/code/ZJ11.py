# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        if n < 0:
            n += 2**32
        count = 0
        num_2 = [0]*32
        index = 31
        while n>2:
            if n%2!=0:
                count += 1
                num_2[index] = 1
            index -= 1
            n = int(n/2)
        if n == 2:
            num_2[index] = 0
            num_2[index-1] = 1
        elif n == 1:
            num_2[index] = 1
        count += 1
        print(num_2)
        return count

if __name__ == '__main__':
    sol = Solution()
    n = 214748367
    print(sol.NumberOf1(n))