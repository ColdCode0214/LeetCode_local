class Solution {
public:
    int minSteps(string s, string t) {
        int l1=s.size(), l2=t.size();
        int ans=0;
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        int a=0, b=0;
        while(a<l1 && b<l2)
        {
            //cout<<"@@@";
            if(s[a]!=t[b])
            {
                //cout<<"^^^";
                ans++;
                if(s[a]<t[b])
                    a++;
                else
                    b++;
            }
            else
            {
                a++;
                b++;
            }
        }
        if(a<l1)
            ans+=l1-a;
        if(b<l2)
            ans+=l2-b;
        return ans;
    }
};
