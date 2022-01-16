class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        int lens=keysPressed.size();
        int temp=releaseTimes[0];
        int temp2=0;
        char ans=keysPressed[0];
        for(int i=1;i<lens;i++)
        {
            temp2=releaseTimes[i]-releaseTimes[i-1];
            if(temp2>temp)
            {
                temp=temp2;
                ans=keysPressed[i];
            }
            else if(temp2==temp)
            {
                if(keysPressed[i]>ans)
                    ans=keysPressed[i];
            }
        }

        return ans;
    }
};
