class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        int m=words.size();
        vector<string> ans;
        ans.push_back(words[0]);
        int flag=0;
        // for(int i=0;i<m;i++)
        // {
        //     flag=0;
        //     for(int j=0;j<ans.size();j++)
        //     {
        //         if(words[i].size()==ans[j].size())
        //         {
        //             string temp=words[i];
        //             string temp2=ans[j];
        //             sort(temp.begin(), temp.end());
        //             sort(temp2.begin(), temp2.end());
        //             if(temp==temp2)
        //             {
        //                 flag=1;
        //                 break;
        //             }
        //         }
        //     }
        //     if(flag==0)
        //         ans.push_back(words[i]);
        // }
        for(int i=1;i<m;i++)
        {
            string temp=words[i];
            string temp2=words[i-1];
            sort(temp.begin(), temp.end());
            sort(temp2.begin(), temp2.end());
            if(temp!=temp2)
                ans.push_back(words[i]);
        }
        return ans;
    }
};
