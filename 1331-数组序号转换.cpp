class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> arr2=arr;
        int lens=arr.size();
        sort(arr.begin(), arr.end());
        unordered_map<int, int> mp;
        int count=1;
        for(int i=0;i<lens;i++)
        {
            if(!mp.count(arr[i]))
            {
                mp[arr[i]]=count;
                count++;
            }
        }
        vector<int> ans;
        for(int i=0;i<lens;i++)
            ans.push_back(mp[arr2[i]]);
        return ans;
    }
};
