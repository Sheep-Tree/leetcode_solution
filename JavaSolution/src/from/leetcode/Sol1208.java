package from.leetcode;

public class Sol1208 {
	public int equalSubstring(String s, String t, int maxCost) {
		int n = s.length();
		if (n == 0) {
			return 0;
		}
		int[] cost = new int[n];
		char[] s_c = s.toCharArray();
		char[] t_c = t.toCharArray();
		int max_str_len = 0;
		for (int i = 0; i < n; i++) {
			cost[i] = Math.abs(s_c[i] - t_c[i]);
		}
		for (int i = 0; i < n; i++) {
			int temp_cost = cost[i];
			if (temp_cost > maxCost) {
				continue;
			}
			for (int j = 1; j + i <= n; j++) {
				if (j + i == n) {
					if (max_str_len < j) {
						max_str_len = j;
					}
				} else {
					temp_cost += cost[i + j];
					if (temp_cost > maxCost) { // 前一个没事
						if (max_str_len < j) {
							max_str_len = j;
						}
						break;
					}
				}
			}
		}
		return max_str_len;
	}

	public void run() {
		String s = "krpgjbjjznpzdfy";
		String t = "nxargkbydxmsgby";
		int maxCost = 14;
		int result = equalSubstring(s, t, maxCost);
		System.out.print(result);
	}
}
