class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int, int> mp;
        int temp=0;
        for(auto& a:arr)
            mp[a]++;
        sort(arr.rbegin(), arr.rend());
        for(int i=0;i<arr.size();i++)
            if(mp[arr[i]]==arr[i])
                return arr[i];
        return -1;
    }
};
