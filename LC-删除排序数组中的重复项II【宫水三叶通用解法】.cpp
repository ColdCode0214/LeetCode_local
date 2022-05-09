class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        return help(nums, 2);
    }
    int help(vector<int>& nums, int k)
    {
        int lens=0;
        for(auto n:nums)
        {
            if(lens<k || nums[lens-k]!=n)
            {
                nums[lens++]=n;//���������ִ�ж���nums[lens]�ĸ�ֵ���ٽ�lens++
                //lens++;�����lens++������������в�����ʱ�临�ӶȽϸ�
            }
                
        }
        return lens;
    }
};
