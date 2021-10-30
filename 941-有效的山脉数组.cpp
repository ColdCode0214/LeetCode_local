class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int lens=arr.size();
        if(lens<3)
            return false;
        int max=0;
        for(int i=0;i<lens;i++)
            if(arr[i]>arr[max])
                max=i;
        if(max==0 || max==lens-1)
            return false;
        for(int i=0;i<max;i++)
            if(arr[i+1]<=arr[i])
                return false;
        for(int j=max+1;j<lens;j++)
            if(arr[j]>=arr[j-1])
                return false;
        return true;
    }
};
