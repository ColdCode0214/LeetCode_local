class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        int mid, sum; 
        vector<int> record;
        //先用二分法找到上界元素，此种方法只在数组中不包含负值时可用 
        while(i < j){
            mid = (i + j)/2;
            if(nums[mid] >= target)
                j = mid - 1;
            else
                i = mid + 1;
        }
        i = 0;
        while(i < j){
            sum = nums[i] + nums[j];
            if(sum > target)
                j--;
            else if(sum < target)
                i++;
            else{
                record.push_back(nums[i]);
                record.push_back(nums[j]);
                break;    
            }
        }
        return record;
    }
};
