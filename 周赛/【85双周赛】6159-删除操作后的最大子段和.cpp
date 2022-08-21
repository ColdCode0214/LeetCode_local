class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        //求前缀和
        int n = nums.size();
        long long int f[n+1];
        f[0] = 0;
        for(int i=1;i<n+1;i++)
            f[i] = f[i-1] + nums[i-1];
        
        //声明记录已删除下标的数据结构并初始化
        set<int> st;
        st.insert(0), st.insert(n+1);

        //声明记录所有子段和的数据结构并初始化
        multiset<long long int> ms;
        ms.insert(f[n]);

        //声明记录答案的变量
        vector<long long> ans;

        //逐一处理query
        for(int pos:removeQueries)
        {
            pos++;
            //找到pos的左右下标LR
            auto it=st.upper_bound(pos);
            int L = *prev(it), R = *it;
            //处理删除下标
            st.insert(pos);
            //更新子段和
            ms.erase(ms.find(f[R-1]-f[L]));
            if(pos-L-1>0)
                ms.insert(f[pos-1]-f[L]);
            if(R-pos-1>0)
                ms.insert(f[R-1]-f[pos]);
            //找出本轮的最大子段和
            if(ms.empty())
                ans.push_back(0);
            else
                ans.push_back(*prev(ms.end()));
        }
        return ans;
    }
};
