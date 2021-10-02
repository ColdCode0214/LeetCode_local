class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int lens=flowerbed.size();
        if(lens==1)
        {
            if(flowerbed[0]+n<=1)
                return true;
            else
                return false;
        }
        for(int i=0;i<lens;i++)
        {
            if(n==0)
                break;
            if(flowerbed[i]==0)
            {
                if(i==0)
                {
                    if(flowerbed[i+1]==0)
                    {
                        n--;
                        flowerbed[i]=1;
                    }
                }
                else if(i==lens-1)
                {
                    if(flowerbed[i-1]==0)
                    {
                        n--;
                        flowerbed[i]=1;
                    }
                }
                else
                {
                    if(flowerbed[i-1]==0 && flowerbed[i+1]==0)
                    {
                        n--;
                        flowerbed[i]=1;
                    }
                }
            }
            
        }
        if(n>0)
            return false;
        else
            return true;
    }
};
