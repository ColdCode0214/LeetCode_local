class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int i=0;
        while(i+1<arr.size() && arr[i+1]>arr[i])
            i++;
        if(i==0 || i==arr.size()-1)
            return false;
        while(i<arr.size()-1 && arr[i]>arr[i+1])
            i++;
        return i==arr.size()-1;
    }
};
