class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        int lens=spaces.size();//��ӿո�����鳤��
        int lens2=s.size();//�ַ�������

        string ans="";

        int p=0;//��Ϊ��ӿո��������±�
        for(int i=0;i<lens2;i++)
        {
            if(p<lens)
            {
                if(i==spaces[p])
                {
                    ans+=' ';
                    //ans+=s[i];
                    p++;
                }
            }
            
            ans+=s[i];
        }
        return ans;
        
    }
};
