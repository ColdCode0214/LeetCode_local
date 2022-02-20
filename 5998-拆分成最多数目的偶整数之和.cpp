class Solution {
public:
    vector<long long> maximumEvenSplit(long long finalSum) {
        vector<long long> ans;
        if(finalSum%2==1)
            return ans;
        int k=2;
        while(finalSum>=k)
        {
            ans.push_back(k);
            finalSum-=k;
            k+=2;
        }
        //cout<<"k:"<<k<<endl;
        int lens2=ans.size();
        //for(int i=0;i<lens2;i++)
        //    cout<<ans[i]<<" ";
        if(finalSum!=0)
        {

            ans[lens2-1]+=finalSum;
            //cout<<"%%%:"<<ans[lens2-1]<<endl;
            //cout<<"@@@:"<<finalSum<<endl;
            //cout<<"###:"<<finalSum/2-1<<endl;
            //ans.erase(ans.begin()+finalSum/2-1);
            //cout<<"k/2-1"<<k/2-1<<endl;
            
        }
        


        return ans;
    }
};
