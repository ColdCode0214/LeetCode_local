class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> ans;
        unordered_map<int, int> mp;
        vector<int> temp;
        int lens1=arr1.size(), lens2=arr2.size();
        for(int a:arr2)
            mp[a]=0;
        for(int a:arr1)
        {
            if(mp.count(a))
                mp[a]++;
            else
                temp.push_back(a);
        }
        sort(temp.begin(), temp.end());
        for(int a:arr2)
        {
            for(int i=0;i<mp[a];i++)
            {
                ans.push_back(a);
            }
        }
        ans.insert(ans.end(), temp.begin(), temp.end());
        return ans;
    }
};
