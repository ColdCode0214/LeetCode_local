class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int lens=arr.size();
        int left=0, right=lens-1;
        for(int i=0;i<lens-1;i++)
        {
            for(int j=lens-1;j>i;j--)
            {
                if(arr[i]*2==arr[j] || arr[j]*2==arr[i])
                    return true;
                if(arr[i]*2>arr[j])
                    break;
            }
            
        }
        return false;
    }
};
