class Solution {
public:
    double average(vector<int>& salary) {
        sort(salary.begin(), salary.end());
        int lens=salary.size();
        double ans=0;
        for(int i=1;i<lens-1;i++)
            ans+=salary[i];
        return ans/(lens-2);
    }
};
