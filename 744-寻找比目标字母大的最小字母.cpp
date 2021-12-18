class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int lens=letters.size();
        for(int i=0;i<lens;i++)
        {
            if(letters[i]>target)
                return letters[i];
        }
        return letters[0];
    }
};
