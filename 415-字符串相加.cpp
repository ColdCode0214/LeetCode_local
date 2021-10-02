class Solution {
public:
    string temp2;//用于存储ASCII码转换的字符
    int jinwei=48;
    string calTemp2(int temp)
    {
        if(temp>=154)//有进位
        {
            jinwei=49;
            temp2=temp-106;
        }
        else//无进位
        {
            jinwei=48;
            temp2=temp-96;
        }
        return temp2;
    }
    string addStrings(string num1, string num2) {
        int lens1=num1.size();
        int lens2=num2.size();
        
        int temp;//用于计算ASCII码值
        string ans="";
        
        for(int i=0;i<min(lens1,lens2);i++)
        {
            temp=jinwei+num1[lens1-1-i]+num2[lens2-1-i];
            temp2=calTemp2(temp);
            ans=temp2+ans;
        }
        if(lens1!=min(lens1,lens2))
        {
            for(int i=lens1-lens2-1;i>=0;i--)
            {
                temp=jinwei+num1[i]+48;
                temp2=calTemp2(temp);
                ans=temp2+ans;
            }

        }
        if(lens2!=min(lens1,lens2))
        {
            for(int i=lens2-lens1-1;i>=0;i--)
            {
                temp=jinwei+num2[i]+48;
                temp2=calTemp2(temp);
                ans=temp2+ans;
            }
        }

        if(jinwei==49)
            ans="1"+ans;
        return ans;
    }
};
