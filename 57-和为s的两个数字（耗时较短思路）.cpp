class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0, j = nums.size() - 1;
        int mid, sum; 
        vector<int> record;
        //���ö��ַ��ҵ��Ͻ�Ԫ�أ����ַ���ֻ�������в�������ֵʱ���� 
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
