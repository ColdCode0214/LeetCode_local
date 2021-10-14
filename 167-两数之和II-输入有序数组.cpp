class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int lens=numbers.size();
        int left=0,right=lens-1;
        vector<int> ans;
        while(left!=right)
        {
            if(numbers[left]+numbers[right]<target)
                left++;
            if(numbers[left]+numbers[right]>target)
                right--;
            if(numbers[left]+numbers[right]==target)
            {
                ans.push_back(left+1);
                ans.push_back(right+1);
                return ans;
            }
        }
        return ans;
    }
};
