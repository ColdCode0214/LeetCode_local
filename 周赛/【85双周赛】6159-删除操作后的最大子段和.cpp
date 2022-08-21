class Solution {
public:
    vector<long long> maximumSegmentSum(vector<int>& nums, vector<int>& removeQueries) {
        //��ǰ׺��
        int n = nums.size();
        long long int f[n+1];
        f[0] = 0;
        for(int i=1;i<n+1;i++)
            f[i] = f[i-1] + nums[i-1];
        
        //������¼��ɾ���±�����ݽṹ����ʼ��
        set<int> st;
        st.insert(0), st.insert(n+1);

        //������¼�����Ӷκ͵����ݽṹ����ʼ��
        multiset<long long int> ms;
        ms.insert(f[n]);

        //������¼�𰸵ı���
        vector<long long> ans;

        //��һ����query
        for(int pos:removeQueries)
        {
            pos++;
            //�ҵ�pos�������±�LR
            auto it=st.upper_bound(pos);
            int L = *prev(it), R = *it;
            //����ɾ���±�
            st.insert(pos);
            //�����Ӷκ�
            ms.erase(ms.find(f[R-1]-f[L]));
            if(pos-L-1>0)
                ms.insert(f[pos-1]-f[L]);
            if(R-pos-1>0)
                ms.insert(f[R-1]-f[pos]);
            //�ҳ����ֵ�����Ӷκ�
            if(ms.empty())
                ans.push_back(0);
            else
                ans.push_back(*prev(ms.end()));
        }
        return ans;
    }
};
