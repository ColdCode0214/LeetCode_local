class Solution {
public:
    string reverseWords(string s) {
        int lens=s.size();
        int i=0;
        while(i<lens)
        {
            int start=i;
            while(i<lens && s[i]!=' ')
                i++;
            int left=start, right=i-1;
            while(left<right)
            {
                swap(s[left], s[right]);
                left++;
                right--;
            }
            while(i<lens && s[i]==' ')
                i++;
        }
        return s;
    }
};
