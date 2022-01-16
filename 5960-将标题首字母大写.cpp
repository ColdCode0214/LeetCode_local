class Solution {
public:
    string capitalizeTitle(string title) {
        int lens=title.size();
        if(lens<=2)
        {
            for(int i=0;i<lens;i++)
                title[i]=tolower(title[i]);
            return title;
        }
        string s2="";
        int temp=0, index=0;
        while(index<lens)
        {
            if(index==lens-1)
                title[index]=tolower(title[index]);
            temp=index+1;
            while(title[temp]!=' ' && temp<lens)
                temp++;
            if(temp-index<=2)
            {
                for(int i=index;i<temp;i++)
                {
                    title[i]=tolower(title[i]);
                }
            }
            else
            {
                //cout<<"^^^^"<<title[index]<<endl;
                title[index]=toupper(title[index]);
                //cout<<"****"<<title[index]<<endl;
                for(int i=index+1;i<temp;i++)
                {
                    title[i]=tolower(title[i]);
                }
            }
            index=temp+1;
        }
        return title;
    }
};
