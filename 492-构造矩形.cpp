class Solution {
public:
    vector<int> constructRectangle(int area) {
        vector<int> ans;
        int L=0, W=sqrt(area);
        while(area%W!=0)
            W--;
        ans.push_back(area/W);
        ans.push_back(W);
        return ans;
    }
};
