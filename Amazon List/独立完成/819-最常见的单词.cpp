class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        transform(paragraph.begin(),paragraph.end(),paragraph.begin(),::tolower); //��дתСд����
        map<string, int> mpbanned;
        int lens=banned.size();
        for(auto& a:banned)
        {
            transform(a.begin(),a.end(),a.begin(),::tolower);
            mpbanned[a]=1;
        }
        int n=paragraph.size();
        string s="";//���ڼ�¼paragraph����ȡ�ĵ���
        map<string, int> ans;//���ڼ�¼paragraph�е��ʳ��ֵĴ���
        for(int i=0;i<n;i++)
        {
            if(!(paragraph[i]>=97&&paragraph[i]<=122))
            {
                if(!mpbanned.count(s)&&s.size()>0)
                    ans[s]++;
                s="";
            }
            else
                s+=paragraph[i];
        }
        if(s.size()>0)
            ans[s]++;
        string res="";
        int num=0;
        for(auto& a:ans)
        {
            if(a.second>num)
            {
                res=a.first;
                num=a.second;
            }
        }
        return res;
    }
};
