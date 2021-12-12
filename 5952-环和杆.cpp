class Solution {
public:
    int countPoints(string rings) {
        int lens=rings.size();
        vector<vector<int>> ans;
        vector<int> temp;
        //cout<<"%%%%%%%%";
        int flag=0;
        for(int i=0;i<lens;i+=2)
        {
            flag=0;
            temp.clear();
            for(int j=0;j<ans.size();j++)
            {
                if(ans[j][0]+48==rings[i+1])
                {
                    //cout<<"ans:"<<ans[j][0]<<endl;
                    //cout<<"ring:"<<rings[i+1]<<endl;
                    if(rings[i]=='R')
                        ans[j][1]=1;
                    if(rings[i]=='G')
                        ans[j][2]=1;
                    if(rings[i]=='B')
                        ans[j][3]=1;
                    flag=1;
                }
            }
            if(flag==0)
            {
                int num=rings[i+1]-48;
                temp.push_back(num);
                temp.push_back(0);
                temp.push_back(0);
                temp.push_back(0);
                ans.push_back(temp);
                for(int j=0;j<ans.size();j++)
                {
                    if(ans[j][0]+48==rings[i+1])
                    {
                        //cout<<"ans:"<<ans[j][0]<<endl;
                        //cout<<"ring:"<<rings[i+1]<<endl;
                        if(rings[i]=='R')
                            ans[j][1]=1;
                        if(rings[i]=='G')
                            ans[j][2]=1;
                        if(rings[i]=='B')
                            ans[j][3]=1;
                        flag=1;
                    }
                }
            }
        }
        int count=0;
        for(int i=0;i<ans.size();i++)
        {
            if(ans[i][1]+ans[i][2]+ans[i][3]==3)
                count++;
        }
        //cout<<"333333";
        /*
        for(int i=0;i<ans.size();i++)
        {
            for(int j=0;j<4;j++)
            {
                cout<<ans[i][j]<<" ";
            }
            cout<<endl;
        }*/
        return count;
    }
};
