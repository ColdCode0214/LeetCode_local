#include<cstring>
#include<algorithm>
class Solution {
public:
    int add(string a,string b,string c,int i)
    {
        //string total;
        int lens_a=a.size();
        int lens_b=b.size();
        int count=0;
        if(a[lens_a-1-i]=='1')
            count++;
        if(b[lens_b-1-i]=='1')
            count++;
        if(c[0]=='1')
            count++;
        return count;
    }
    string addBinary(string a, string b) {
        int lens_a=a.size();
        int lens_b=b.size();
        int num=0;
        string ans;
        string c="0";
        for(int i=0;i<max(lens_a,lens_b);i++)
        {
            //c='0';
            if(i<lens_a&&i<lens_b)
            {
                num=add(a,b,c,i);
                if(num==0)
                {
                    ans='0'+ans;
                    c='0';
                }
                if(num==1)
                {
                    ans='1'+ans;
                    c='0';
                }
                if(num==2)
                {
                    ans='0'+ans;
                    c='1';
                }
                if(num==3)
                {
                    ans='1'+ans;
                    c='1';
                }
            }
            else if(i>=lens_a&&i<lens_b)
            {
                if(c[0]=='0')
                    ans=b[lens_b-1-i]+ans;
                else
                {
                    if(b[lens_b-1-i]=='0')
                    {
                        ans='1'+ans;
                        c='0';
                    }
                    else
                        ans='0'+ans;
                }
            }
            else if(i>=lens_b&&i<lens_a)
            {
                if(c[0]=='0')
                    ans=a[lens_a-1-i]+ans;
                else
                {
                    if(a[lens_a-1-i]=='0')
                    {
                        ans='1'+ans;
                        c='0';
                    }
                    else
                        ans='0'+ans;
                }
            }
        }
        if(c[0]=='1')
            ans='1'+ans;
        return ans;
    }
};
