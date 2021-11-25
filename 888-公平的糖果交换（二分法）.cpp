class Solution {
public:
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        int sa=accumulate(aliceSizes.begin(), aliceSizes.end(), 0);
        int sb=accumulate(bobSizes.begin(), bobSizes.end(), 0);
        sort(bobSizes.begin(), bobSizes.end());
        int diff=(sb-sa)/2;
        //cout<<"sa:"<<sa<<endl;
        //cout<<"sb:"<<sb<<endl;
        vector<int> ans(2);
        for(auto& a:aliceSizes)
        {
            int l=0, r=bobSizes.size()-1;
            
            int b=a+diff;
            //cout<<"a:"<<a<<endl;
            //cout<<"diff"<<diff<<endl;
            //cout<<"b:"<<b<<endl;
            while(l<r)
            {
                int mid=(l+r)/2;
                if(bobSizes[mid]>=b)
                    r=mid;
                else
                    l=mid+1;
            }
            if(bobSizes[l]==b)
                return vector<int>{a,b};
        }
        return ans;
    }
};
