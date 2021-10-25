class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> ans;
        int j=0, temp=0;
        int flag=0;
        for(int i=left;i<=right;i++)
        {
            j=i;
            flag=1;
            while(j>0)
            {
                temp=j%10;
                if(temp==0 || i%temp!=0)
                {
                    flag=0;
                    break;
                }
                j/=10;
            }
            if(flag==1)
                ans.push_back(i);
        }
        return ans;
    }
};
