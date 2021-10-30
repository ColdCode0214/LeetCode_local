class Solution {
public:
    int maximum69Number (int num) {
        vector<int> ans;
        while(num>0)
        {
            ans.push_back(num%10);
            num/=10;
        }
        int flag=0;
        for(int i=ans.size()-1;i>=0;i--)
        {
            if(ans[i]==6 && flag==0)
            {
                ans[i]=9;
                flag=1;
            }
            num*=10;
            num+=ans[i];
        }
        return num;
    }
};
