class Solution {
public:
    bool judgeSquareSum(int c) {
        int a=sqrt(c);
        int b=0;
        while(a>=b)
        {
            b=sqrt(c-a*a);
            if(a*a+b*b==c)
                return true;
            a--;
        }
        return false;
    }
};
