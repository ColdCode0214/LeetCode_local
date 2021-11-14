class Solution {
public:
    bool checkAlmostEquivalent(string word1, string word2) {
        int lens=word1.size();
        for(int i=0;i<lens;i++)
        {
            for(int j=0;j<lens;j++)
            {
                if(word1[i]==word2[j])
                {
                    word1[i]='0';
                    word2[j]='0';
                    break;
                }
            }   
        }
        cout<<"word1:"<<word1<<endl;
        cout<<"word2:"<<word2<<endl;
        string a, b;
        for(int i=0;i<lens;i++)
        {
            if(word1[i]!='0')
                a+=word1[i];
            if(word2[i]!='0')
                b+=word2[i];
            
        }
        cout<<"a:"<<a<<endl;
        cout<<"b:"<<b<<endl;
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        cout<<"a2:"<<a<<endl;
        cout<<"b2:"<<b<<endl;
        int count=0;
        for(int i=1;i<a.size();i++)
        {
            if(a[i]==a[i-1])
            {
                count++;
                cout<<"count:"<<count<<endl;
            }
                //count++;
            else
                count=0;
            if(count==3)
                return false;
        }
        count=0;
        for(int i=1;i<b.size();i++)
        {
            if(b[i]==b[i-1])
                count++;
            else
                count=0;
            if(count==3)
                return false;
        }
        return true;
                
    }
};
