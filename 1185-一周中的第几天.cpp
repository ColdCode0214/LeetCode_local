class Solution {
public:
    bool runnian(int year)
    {
        if((year%4==0 && year%100!=0) || year%400==0)
            return true;
        return false;
    }
    string dayOfTheWeek(int day, int month, int year) {
        int run=0;
        string weekday[7]={"Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"};
        
        int sum=0;
        for(int i=1971;i<year;i++)
        {
            if(runnian(i)==true)
                sum+=366;
            else
                sum+=365;
        }
        //cout<<"sum0:"<<sum<<endl;
        for(int i=1;i<month;i++)
        {
            if(i==2)
            {
                if(runnian(year)==0)
                    sum+=28;
                else
                {
                    sum+=29;
                    //cout<<"***"<<endl;
                }
                    //sum+=29;
            }
            else if(i<=7)
            {
                if(i%2==1)
                    sum+=31;
                else
                    sum+=30;
            }
            else
            {
                if(i%2==1)
                    sum+=30;
                else
                    sum+=31;
            }
            
        }
        //cout<<"sum1:"<<sum<<endl;
        sum+=day;
        //cout<<"sum2:"<<sum<<endl;
        int index=sum-sum/7*7;
        if(index==0)
            return weekday[6];
        return weekday[index-1];
    }
};
