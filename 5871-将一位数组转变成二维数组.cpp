class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        int lens=original.size();
        vector<vector<int>> ans;
        vector<int> temp;
        if(lens!=m*n)
            return ans;
        for(int i=0;i<m;i++)
        {
            temp.clear();
            for(int j=0;j<n;j++)
                temp.push_back(original[i*n+j]);
            ans.push_back(temp);
        }
        return ans;
    }
};
