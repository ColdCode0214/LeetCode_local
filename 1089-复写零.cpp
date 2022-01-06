class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int lens=arr.size();
        vector<int> temp;
        for(int i=0;i<lens;i++)
        {
            temp.push_back(arr[i]);
            if(arr[i]==0)
                temp.push_back(0);
            if(temp.size()==lens)
                break;
        }
        for(int i=0;i<lens;i++)
            arr[i]=temp[i];
        return;
    }
};
