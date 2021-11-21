class Solution {
public:
    bool isHappy(int n) {
        int ans=0;
        vector<int> rec;
        rec.push_back(n);
        while(1)
        {
            while(n>0)
            {
                ans+=pow(n%10, 2);
                n/=10;
            }
            if(ans==1)
                return true;
            for(int i=0;i<rec.size();i++)
                if(ans==rec[i])
                    return false;
            rec.push_back(ans);
            n=ans;
            ans=0;
        }
        return true;
    }
};
