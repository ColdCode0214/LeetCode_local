class Solution {
public:
    bool isFlipedString(string s1, string s2) {
        int l1=s1.size(), l2=s2.size();
        if(l1!=l2)
            return false;
        string::size_type pos;
        string temp=s2+s2;
        pos=temp.find(s1);
        if(pos==temp.npos)
            return false;
        return true;
    }
};
