class Solution {
public:
    vector<int> sortEvenOdd(vector<int>& nums) {
        int lens=nums.size();
        vector<int> o,e;
        for(int i=0;i<lens;i+=2)
        {
            e.push_back(nums[i]);
        }
        for(int i=1;i<lens;i+=2)
        {
            o.push_back(nums[i]);
        }
        for(int i=0;i<o.size();i++)
            cout<<o[i]<<" ";
        cout<<endl;
        sort(e.begin(), e.end());
        sort(o.begin(), o.end());
        vector<int> ans;
        for(int i=0;i<lens/2;i++)
        {
            ans.push_back(e[i]);
            ans.push_back(o[o.size()-1-i]);
        }
        if(lens%2==1)
        {
            ans.push_back(e[e.size()-1]);
        }
        for(int i=0;i<o.size();i++)
            cout<<o[i]<<" ";
        return ans;
    }
};
