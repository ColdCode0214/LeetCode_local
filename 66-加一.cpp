class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int num=0;
        int lens=digits.size();
        vector<int> ans;
        int enter=0;
        for(int i=lens-1;i>=0;i--)
        {
            if(i==lens-1)
            {
                if(digits[i]+1 == 10)
                {
                    ans.insert(ans.begin(),0);
                    enter=1;
                }
                else
                {
                    ans.insert(ans.begin(),digits[i]+1);
                    enter=0;
                }
            }
            else
            {
                if(digits[i]+enter==10)
                {
                    ans.insert(ans.begin(),0);
                    enter=1;
                }
                else
                {
                    ans.insert(ans.begin(),digits[i]+enter);
                    enter=0;
                }
            }
        }
        if(enter==1)
            ans.insert(ans.begin(),1);
        return ans;
    }
};
