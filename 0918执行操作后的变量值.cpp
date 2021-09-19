class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int lens=operations.size();
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            if(operations[i][0]=='+'||operations[i][2]=='+')
                ans++;
            else if(operations[i][0]=='-'||operations[i][2]=='-')
                ans--;
        }
        return ans;
    }
};