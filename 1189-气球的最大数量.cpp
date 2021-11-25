
class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int s[5]={0};
        for(char a:text)
        {
            switch(a)
            {
                case 'a': s[0]++;break;
                case 'b': s[1]++;break;
                case 'l': s[2]++;break;
                case 'n': s[3]++;break;
                case 'o': s[4]++;break;
            }
        }
        s[2]/=2;
        s[4]/=2;
        int ans=s[0];
        for(auto& i:s)
        {
            ans=min(ans, i);
            cout<<"i:"<<i<<endl;
        }
            
        return ans;
    }
};
