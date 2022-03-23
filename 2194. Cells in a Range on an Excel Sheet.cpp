class Solution {
public:
    vector<string> cellsInRange(string s) {
        vector<string> ans;
        int rs=0, re=0, cs=0, ce=0;
        rs=s[1]-48;
        re=s[4]-48;
        cs=s[0]-65;
        ce=s[3]-65;
        //int num=(re-rs+1)*(ce-cs+1);
        for(int j=0;j<ce-cs+1;j++)
        {
            
            for(int i=0;i<re-rs+1;i++)
            {
                string temp="";
                char a=65+j+cs;
                char b=48+i+rs;
                temp=temp+a+b;
                ans.push_back(temp);
            }
        }
        return ans;
    }
};
