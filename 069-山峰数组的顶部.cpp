class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int lens=arr.size();
        if(lens<3)
            return 0;
        int maxindex=0;
        int max=arr[0];
        for(int i=1;i<lens;i++)
        {
            if(arr[i]>max)
            {
                max=arr[i];
                maxindex=i;
            }
        }
        return maxindex;
    }
};
