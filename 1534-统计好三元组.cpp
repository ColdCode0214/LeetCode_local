class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int ans=0;
        int lens=arr.size();
        for(int i=0;i<lens-2;i++)
        {
            for(int j=i+1;j<lens-1;j++)
            {
                if(abs(arr[i]-arr[j])<=a)
                {
                    for(int k=j+1;k<lens;k++)
                    {
                        if(abs(arr[j]-arr[k])<=b && abs(arr[i]-arr[k])<=c)
                            ans++;
                    }
                }
            }
        }
        return ans;
    }
};
