class Solution {
public:
    int calPoints(vector<string>& ops) {
        int lens=ops.size();
        int ans=0;
        vector<int> temp;
        for(int i=0;i<lens;i++)
        {
            if(ops[i]=="+")
            {
                temp.push_back(temp[temp.size()-1]+temp[temp.size()-2]);
            }
            else if(ops[i]=="D")
            {
                temp.push_back(temp[temp.size()-1]*2);
            }
            else if(ops[i]=="C")
            {
                temp.pop_back();
            }
            else
            {
                if(ops[i][0]=='-')
                {
                    int lens2=ops[i].size();
                    int temp2=0;
                    for(int j=1;j<lens2;j++)
                    {
                        temp2*=10;
                        temp2+=(ops[i][j]-48);
                    }
                    
                    temp.push_back(-temp2);
                }

                else
                {
                    int lens2=ops[i].size();
                    //cout<<"size:"<<ops[i].size()<<endl;
                    int temp2=0;
                    for(int j=0;j<lens2;j++)
                    {
                        temp2*=10;
                        //cout<<ops[i][j]<<endl;
                        temp2+=(ops[i][j]-48);
                    }
                    //cout<<"temp2:"<<temp2<<endl;
                    temp.push_back(temp2);
                }
            }
        }
        for(int i=0;i<temp.size();i++)
        {
            ans+=temp[i];
            //cout<<temp[i]<<" ";
        }
            
        return ans;
    }
};
