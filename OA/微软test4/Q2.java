// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
import java.util.HashMap;
class Solution {
    public int solution(int[] A) {
        // write your code in Java 11 (Java SE 11)
        HashMap<Integer,Integer> map=new HashMap<>();
        map.put(0,1);
        int sum=0;
        int res=0;
        for(int i:A){
            sum+=i;
            if(map.containsKey(sum-0)){
                res+=map.get(sum);
            }
            map.put(sum,map.getOrDefault(sum,0)+1);
        }
        
        return res>100000000?-1:res;
    }
}
