class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> heap;
        for(auto& x:nums)
        {
            heap.push(x);
            if(heap.size()>k)
                heap.pop();
        }
        return heap.top();
            
    }
};
