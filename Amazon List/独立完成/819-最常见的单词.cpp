class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        transform(paragraph.begin(),paragraph.end(),paragraph.begin(),::tolower); //大写转小写函数
        map<string, int> mpbanned;
        int lens=banned.size();
        for(auto& a:banned)
        {
            transform(a.begin(),a.end(),a.begin(),::tolower);
            mpbanned[a]=1;
        }
        int n=paragraph.size();
        string s="";//用于记录paragraph中提取的单词
        map<string, int> ans;//用于记录paragraph中单词出现的次数
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
