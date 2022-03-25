class Solution {
public:
    int minArray(vector<int>& numbers) {
        int lens=numbers.size();
        for(int i=0;i<lens-1;i++)
        {
            if(numbers[i+1]<numbers[i])
                return numbers[i+1];
        }
        return numbers[0];
    }
};
