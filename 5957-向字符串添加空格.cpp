class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int lens=spaces.size();//添加空格的数组长度
        int lens2=s.size();//字符串长度

        string ans="";

        int p=0;//作为添加空格的数组的下标
        for(int i=0;i<lens2;i++)
        {
            if(p<lens)
            {
                if(i==spaces[p])
                {
                    ans+=' ';
                    //ans+=s[i];
                    p++;
                }
            }
            
            ans+=s[i];
        }
        return ans;
        
    }
};
