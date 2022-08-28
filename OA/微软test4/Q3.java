// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] A) {
        // write your code in Java 11 (Java SE 11)
        int n=A.length;
        if(n<=1) return 0;
        int[] dp=new int[n+1];
        int res=0;
        for(int i=0;i<n;i++){
            if(i<2){
                dp[i]=0;
                continue;
            }
            if(A[i]-A[i-1]==A[i-1]-A[i-2]){
                dp[i]=dp[i-1]+1;
                res+=dp[i];
            }
        }
        return res > 1000000000 ? -1:res;
    }
}
