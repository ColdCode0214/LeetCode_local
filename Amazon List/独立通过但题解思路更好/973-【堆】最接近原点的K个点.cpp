class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //堆（优先队列）(C++默认大根堆，python默认小根堆【可通过取负值转为“大根堆”】)
        priority_queue<pair<int, int>> q; //第一个int存距离的平方，第二个int存编号
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
