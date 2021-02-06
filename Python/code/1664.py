class Solution:
    def waysToMakeFair(self, nums)
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + (nums[i-1] if i % 2 else -nums[i-1])

        ans = 0
        for i in range(1, n + 1):
            if dp[i - 1] == dp[n] - dp[i]:
                ans += 1
        return ans

if __name__ == '__main__':
	sol = Solution()
	nums = [6,1,7,4,1]
	print(sol.waysToMakeFair(nums))