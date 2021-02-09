package from.leetcode;

public class Sol978 {
	public int maxTurbulenceSize(int[] arr) {
		int n = arr.length;
		int[][] dp = new int[n][2];
		dp[0][0] = 1;
		dp[0][1] = 1;
		for (int i = 1; i < n; i++) {
			dp[i][0] = 1;
			dp[i][1] = 1;
			if (arr[i] > arr[i - 1]) {
				dp[i][0] = dp[i - 1][1] + 1;
			} else if (arr[i] < arr[i - 1]) {
				dp[i][1] = dp[i - 1][0] + 1;
			}
		}
		int max_t = 1;
		for (int i = 0; i < n; i++) {
			max_t = Math.max(dp[i][0], max_t);
			max_t = Math.max(dp[i][1], max_t);
		}
		return max_t;
	}

	public void run() {
		int[] arr = { 9, 4, 2, 10, 7, 8, 8, 1, 9 };
		// int[] arr = { 9, 9 };
		System.out.print(maxTurbulenceSize(arr));
	}
}
