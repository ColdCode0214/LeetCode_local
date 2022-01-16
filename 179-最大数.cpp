class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> cpy;
        for(auto& x:nums)
            cpy.push_back(to_string(x));
        sort(cpy.begin(), cpy.end(), [](const string& a, const string& b) {return a+b > b+a;});
        if(cpy[0]=="0")
            return "0";
        string ans="";
        for(auto& x:cpy)
            ans+=x;
        return ans;
    }
};
