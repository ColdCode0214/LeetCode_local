class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int lens=fruits.size();
        int left=0;
        int count=0,ans=0;
        unordered_map<int, int> basket;
        for(int i=0;i<lens;i++)
        {
            basket[fruits[i]]++;
            count++;
            if(basket.size()>2)
            {
                basket[fruits[left]]--;
                if(basket[fruits[left]]==0)
                {
                    basket.erase(fruits[left]);
                }
                left++;
                count--;
            }
            if(count>ans)
                ans=count;
        }
        return ans;
    }
};
