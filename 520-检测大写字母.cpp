class Solution {
public:
    bool detectCapitalUse(string word) {
        int lens=word.size();
        int flag=0;
        int count=0;
        for(int i=0;i<lens;i++)
        {
            if(word[i]>=97)
                flag=1;
            else
                count++;
            if((flag==1 && word[i]<97) || (count>=2 && word[i]>=97))
                return false;
        }
        return true;
    }
};
