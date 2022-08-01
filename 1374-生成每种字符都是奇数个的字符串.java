class Solution {
    public String generateTheString(int n) {
        StringBuffer sb = new StringBuffer();
        if(n%2==1)
        {
            return sb.append("a".repeat(n)).toString();
        }
        return sb.append("a".repeat(n-1)).append("b").toString();
    }
}