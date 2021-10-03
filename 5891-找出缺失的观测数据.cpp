class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        vector<int> ans;
        int m=rolls.size();
        int sum=mean*(m+n);
        int sum_m=0;
        for(int i=0;i<m;i++)
            sum_m+=rolls[i];
        int sum_n=sum-sum_m;
        if(sum_n>6*n || sum_n<1*n)
            return ans;
        int ans2[n];
        int temp=sum_n/n;//求平均每个n中的元素大概是多大，向下取整
        for(int i=0;i<n;i++)
            ans2[i]=temp;
        int sum_n2=temp*n;//求如果向下取整实际值是多少
        int diff=sum_n-sum_n2;//求差值
        int p=0;
        while(diff>0)
        {
            ans2[p]++;
            p++;
            if(p==n)
                p=0;
            diff--;
        }
        for(int i=0;i<n;i++)
            ans.push_back(ans2[i]);
        return ans;
    }
};
