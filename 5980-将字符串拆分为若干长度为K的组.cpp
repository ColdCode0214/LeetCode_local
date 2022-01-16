class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int lens=s.size();
        vector<string> ans;
        string temp;
        for(int i=0;i<lens;i+=k)
        {
            temp="";
            for(int j=0;j<k;j++)
            {
                if(ans.size()*k+j<lens)
                {
                    temp+=s[i+j];
                }
                else
                    temp+=fill;
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
