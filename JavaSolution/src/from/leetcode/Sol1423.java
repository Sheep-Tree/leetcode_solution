package from.leetcode;
import java.util.Arrays;

public class Sol1423 {
	    public int maxScore(int[] cardPoints, int k) {
	        //问题转换 求剩下的连续的n个的最小值
	    	int n = cardPoints.length;
	    	int x = n-k;
	    	int first_sum = 0;
	    	//计算第一个滑动窗口的值
	    	for(int i=0;i<x;i++) {
	    		first_sum += cardPoints[i];
	    	}
	    	int min_sum = first_sum;
	    	for(int i=1;i<=n-x;i++) {
	    		first_sum = first_sum-cardPoints[i-1]+cardPoints[i+x-1];
	    		min_sum = first_sum<min_sum?first_sum:min_sum;
	    	}
	    	return Arrays.stream(cardPoints).sum()-min_sum;
	    }
	    
	    public void run() {
	    	int[] cardPoints = {96,90,41,82,39,74,64,50,30};
	    	int k = 8;
	    	int result = maxScore(cardPoints,k);
	    	System.out.print(result);
	    }
}
