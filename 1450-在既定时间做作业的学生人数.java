class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        int ans = 0;
        int lens = startTime.length;
        for(int i=0;i<lens;i++)
        {
            if(startTime[i]<=queryTime && endTime[i]>=queryTime)
                ans++;
        }
        return ans;
    }
}