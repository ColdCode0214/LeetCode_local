class Solution {
public:
    int convertTime(string current, string correct) {
        int ans=0;
        int hour1=0, min1=0;
        int hour2=0, min2=0;
        hour1=(current[0]-48)*10+(current[1]-48);
        min1=(current[3]-48)*10+(current[4]-48);
        hour2=(correct[0]-48)*10+(correct[1]-48);
        min2=(correct[3]-48)*10+(correct[4]-48);
        int diff=0;
        diff=(hour2-hour1)*60+(min2-min1);
        cout<<"diff:"<<diff<<endl;
        while(diff>=60)
        {
            diff-=60;
            ans++;
        }
        while(diff>=15)
        {
            diff-=15;
            ans++;
        }
        while(diff>=5)
        {
            diff-=5;
            ans++;
        }
        while(diff>=1)
        {
            diff-=1;
            ans++;
        }
        return ans;
    }
};
