package from.leetcode;

import java.util.Arrays;

public class Sol567 {
	public boolean checkInclusion(String s1, String s2) {
		int s1_len = s1.length();
		int s2_len = s2.length();
		if (s1_len > s2_len) {
			return false;
		}
		int[] count1 = new int[26];
		int[] count2 = new int[26];
		// 针对第一个窗口进行一次统计
		for (int i = 0; i < s1_len; i++) {
			count1[s1.charAt(i) - 'a']++;
			count2[s2.charAt(i) - 'a']++;
		}
		if (Arrays.equals(count1, count2)) {
			return true;
		}
		for (int i = 1; i < s2_len - s1_len + 1; i++) {
			count2[s2.charAt(i - 1) - 'a']--;
			count2[s2.charAt(i + s1_len - 1) - 'a']++;
			if (Arrays.equals(count1, count2)) {
				return true;
			}
		}
		return false;
	}

	public void run() {
		String s1 = "ab";
		String s2 = "eidbaooo";
		System.out.print(checkInclusion(s1, s2));
	}
}
