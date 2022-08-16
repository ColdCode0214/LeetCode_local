class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int n=coordinates.length;
        if(n<=2) return true;
        for(int i=0;i<n-2;i++)
        {
            if((coordinates[i][0]-coordinates[i+1][0])*(coordinates[i+2][1]-coordinates[i+1][1]) != (coordinates[i+2][0]-coordinates[i+1][0])*(coordinates[i][1]-coordinates[i+1][1]))
                return false;
        }
        return true;
    }
}