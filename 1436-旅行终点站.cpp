class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        int lens=paths.size();
        string ans;
        int flag = 0;
        for(int i=0;i<lens;i++)
        {
            flag = 0;
            for(int j=0;j<lens;j++)
            {
                if(paths[i][1] == paths[j][0])
                {
                    flag = 1;
                    break;
                }
            }
            if(flag ==0 )
            {
                ans = paths[i][1];
                break;
            }
        }
        return ans;
    }
};
