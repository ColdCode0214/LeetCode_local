class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> ans, res;
        int lens1=arr1.size(), lens2=arr2.size();
        unordered_map<int, int> mp;
        for(int i=0;i<lens2;i++)
        {
            mp[arr2[i]]=0;
        }
        for(int i=0;i<lens1;i++)
        {
            if(mp.count(arr1[i]))
                mp[arr1[i]]++;
            else
                res.push_back(arr1[i]);
        }
        sort(res.begin(), res.end());
        for(int i=0;i<lens2;i++)
        {
            for(int j=0;j<mp[arr2[i]];j++)
                ans.push_back(arr2[i]);
        }
        ans.insert(ans.end(), res.begin(), res.end());
        return ans;

    }
};
