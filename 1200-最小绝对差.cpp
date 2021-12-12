class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int lens=arr.size();
        int diff_min=arr[1]-arr[0];
        vector<vector<int>> ans;
        vector<int> temp;
        for(int i=0;i<lens-1;i++)
        {
            int diff=arr[i+1]-arr[i];
            if(diff==diff_min)
            {
                temp.push_back(arr[i]);
                temp.push_back(arr[i+1]);
                ans.push_back(temp);
            }
            else if(diff<diff_min)
            {
                diff_min=diff;
                ans.clear();
                temp.push_back(arr[i]);
                temp.push_back(arr[i+1]);
                ans.push_back(temp);
            }
            temp.clear();
        }
        return ans;
    }
};
