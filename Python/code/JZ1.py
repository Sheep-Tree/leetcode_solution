# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        height = len(array)
        width = len(array[0])
        right_all = width-1
        for i in range(height):
            right = right_all
            left = 0
            while left<=right:
                middle = int((right + left)/2)
                if middle == left:
                    if target > array[i][left] and target < array[i][right]:
                        right_all = left
                        break
                    elif target > array[i][right]:
                        break
                    elif target < array[i][left]:
                        right_all = left - 1
                        break
                if target > array[i][middle]:
                    left = middle + 1
                elif target < array[i][middle]:
                    right = middle - 1
                else:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    target = 7
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    array1 = [[]]
    print(sol.Find(target,array1))