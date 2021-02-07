package from.leetcode;

import java.util.Arrays;

public class Sol643 {
	public double findMaxAverage(int[] nums, int k) {
		int n = nums.length;
		if (n == 0) {
			return 0;
		}
		if (k >= n) {
			return Arrays.stream(nums).sum() / (double) n;
		}
		int windows_sum = 0;
		for (int i = 0; i < k; i++) {
			windows_sum += nums[i];
		}
		int max_sum = windows_sum;
		for (int i = 1; i + k - 1 < n; i++) {
			windows_sum = windows_sum - nums[i - 1] + nums[i + k - 1];
			if (windows_sum > max_sum) {
				max_sum = windows_sum;
			}
		}
		return max_sum / (double) k;
	}

	public void run() {
		int[] nums = { 1, 12, -5, -6, 50, 3 };
		int k = 4;
		System.out.print(findMaxAverage(nums, k));
	}
}
