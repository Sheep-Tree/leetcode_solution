package from.leetcode;

public class Sol665 {
	public boolean checkPossibility(int[] nums) {
		boolean change = false;
		for (int i = 1; i < nums.length; i++) {
			if (nums[i] >= nums[i - 1]) {
				continue;
			} else {
				if (change) {
					return false;
				} else {
					if (i - 1 <= 0 || i + 1 >= nums.length) {
						change = true;
					} else if (nums[i] >= nums[i - 2] || nums[i - 1] <= nums[i + 1]) {
						change = true;
					} else {
						return false;
					}
				}
			}
		}
		return true;
	}

	public void run() {
		// int[] nums = { 4, 2, 3 };
		int[] nums = { -1, 4, 2, 3 };
		boolean result = checkPossibility(nums);
		System.out.print(result);
	}
}
