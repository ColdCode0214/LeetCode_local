class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        int lens=points.size();
        map<int, vector<vector<int>>> mp;
        for(int i=0;i<lens;i++)
        {
            vector<int> temp;
            temp.push_back(points[i][0]);
            temp.push_back(points[i][1]);
            int length=points[i][0]*points[i][0]+points[i][1]*points[i][1];
            mp[length].push_back(temp);

        }
        vector<vector<int>> ans;
        for(auto& a:mp)
        {
            if(k>0)
            {
                for(auto& x:a.second)
                {
                    ans.push_back(x);
                    k--;
                }                  
            }
            else
                break;
        }
        return ans;
    }
};
