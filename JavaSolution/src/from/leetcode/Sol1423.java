package from.leetcode;
import java.util.Arrays;

public class Sol1423 {
	    int sum_max = 0;
	    public int maxScore(int[] cardPoints, int k) {
	        if (k >= cardPoints.length){
	            int sum = 0;
	            for(int num:cardPoints){
	                sum += num;
	            }
	            return sum;
	        }
	        backtrack(cardPoints,k,0);
	        return sum_max;
	    }

	    public void backtrack(int[] cardPoints, int k, int sum){
	        if(k == 1){
	            sum += cardPoints[0]>cardPoints[cardPoints.length-1]?cardPoints[0]:cardPoints[cardPoints.length-1];
	            if(sum > sum_max){
	                sum_max = sum;
	            }
	        }else{
	            backtrack(Arrays.copyOfRange(cardPoints,1,cardPoints.length-1),k-1,sum+cardPoints[0]);
	            backtrack(Arrays.copyOfRange(cardPoints,0,cardPoints.length-2),k-1,sum+cardPoints[cardPoints.length-1]);
	        }
	    }
}
