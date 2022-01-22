class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        int lens=differences.size();
        vector<long long int> arr;
        arr.push_back(0);
        int ans=0;
        for(int i=0;i<lens;i++)
        {
            //if(differences[i]+arr[arr.size()-1]>upper)
            //    return 0;
            //else
                arr.push_back(differences[i]+arr[arr.size()-1]);
        }
        sort(arr.begin(), arr.end());
        int l=arr[0], u=arr[lens];
        int diff=lower-l;
        //cout<<"l:"<<l<<endl;
        //cout<<"diff:"<<diff<<endl;
        ans=upper-(u+diff)+1;
        if(ans<0)
            return 0;
        return ans;
    }
};
