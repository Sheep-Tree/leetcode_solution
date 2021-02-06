class solution:
    def waysToStep(self, n):
        one = 1
        two = 2
        three = 4
        ways = 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        for i in range(4,n+1):
            ways = (one + two + three) % 1000000007
            one = two
            two = three
            three = ways
        return ways
if __name__ == '__main__':
    sol = solution()
    print(sol.waysToStep(900750))