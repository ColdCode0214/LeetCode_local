class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> q2, q3, ans;
        vector<long long int> q5;
        int a=0, b=0;
        long long int min_num=0,c=0;
        ans.push_back(1);//第一个丑数是1
        q2.push_back(2);
        q3.push_back(3);
        q5.push_back(5);
        while(ans.size()<n)
        {
            a=q2[0], b=q3[0], c=q5[0];
            min_num=min(a,b);
            min_num=min(min_num,c);
            if(min_num==a && ans[ans.size()-1]!=a)//2倍的队列中
            {
                q2.erase(q2.begin());
                ans.push_back(min_num);
                q2.push_back(min_num*2);
                q3.push_back(min_num*3);
                q5.push_back(min_num*5);
            }
            else if(min_num==b)//3倍的队列中
            {
                q3.erase(q3.begin());
                if(ans[ans.size()-1]!=b)
                {
                    ans.push_back(min_num);
                    q2.push_back(min_num*2);
                    q3.push_back(min_num*3);
                    q5.push_back(min_num*5);
                }
                
            }
            else if(min_num==c)//5倍的队列中
            {
                q5.erase(q5.begin());
                if(ans[ans.size()-1]!=c)
                {
                    ans.push_back(min_num);
                    q2.push_back(min_num*2);
                    q3.push_back(min_num*3);
                    q5.push_back(min_num*5);
                }
                
            }
        }
        return ans[n-1];
    }
};
