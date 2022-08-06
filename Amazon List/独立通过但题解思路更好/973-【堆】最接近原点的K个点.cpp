class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //�ѣ����ȶ��У�(C++Ĭ�ϴ���ѣ�pythonĬ��С���ѡ���ͨ��ȡ��ֵתΪ������ѡ���)
        priority_queue<pair<int, int>> q; //��һ��int������ƽ�����ڶ���int����
        for(int i=0;i<k;i++)
            q.emplace(points[i][0]*points[i][0]+points[i][1]*points[i][1], i);
        int n=points.size();
        for(int i=k;i<n;i++)
        {
            int dist=points[i][0]*points[i][0]+points[i][1]*points[i][1];
            if(dist<q.top().first)
            {
                q.pop();
                q.emplace(dist, i);
            }
        }
        vector<vector<int>> ans;
        while(!q.empty())
        {
            ans.push_back(points[q.top().second]);
            q.pop();
        }
        return ans;
    }
};
