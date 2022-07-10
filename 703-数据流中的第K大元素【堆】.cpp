class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> heap;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k=k;
        for(auto& x:nums)
            add(x);
    }
    
    int add(int val) {
        heap.push(val);
        while(heap.size()>k)
            heap.pop();
        return heap.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
