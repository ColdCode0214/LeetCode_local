class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        vector<int> ans(k,0);
        if(k==0)
            return ans;
        priority_queue<int> Q;
        for(int i=0;i<k;i++)
            Q.push(arr[i]);
        for(int i=k;i<(int)arr.size();i++)
        {
            if(arr[i]<Q.top())
            {
                Q.pop();
                Q.push(arr[i]);
            }
        }
        for(int i=0;i<k;i++)
        {
            ans[i]=Q.top();
            Q.pop();
        }
        return ans;
    }
};
