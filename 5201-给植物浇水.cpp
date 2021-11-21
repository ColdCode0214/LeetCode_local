class Solution {
public:
    int wateringPlants(vector<int>& plants, int capacity) {
        int lens=plants.size();
        int ans=0;
        int cur=capacity;
        for(int i=0;i<lens;i++)
        {
            if(cur>=plants[i])
            {
                ans++;//更新步数
                cur-=plants[i];//更新水量
                //cout<<"ans1:"<<ans<<endl;
            }
            else
            {
                ans+=(i-1-(-1))*2+1;
                cur=capacity-plants[i];
                //cout<<"ans2:"<<ans<<endl;
            }
        }
        return ans;
    }
};
