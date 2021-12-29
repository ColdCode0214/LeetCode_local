class Solution {
public:
    int numFriendRequests(vector<int>& ages) {
        int lens=ages.size();
        if(lens==1)
            return 0;
        int ans=0;
        int temp=0;
        sort(ages.rbegin(), ages.rend());
        for(int i=0;i<lens;i++)
        {
            if(ages[i]<=14)
                break;
            if(!(i>0 && ages[i]==ages[i-1]))
            {
                //cout<<"break1"<<endl;
                temp=0;
                for(int j=i+1;j<lens;j++)
                {
                    if(ages[j]<=14)
                        break;
                    if(ages[j]>0.5*ages[i]+7 && ages[j]<=ages[i])
                        temp++;
                    else
                        break;
                }
            }
            //cout<<"temp:"<<temp<<endl;
            ans+=temp;
        }
        return ans;
    }
};
