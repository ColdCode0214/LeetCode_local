class Solution {
public:
    bool winnerOfGame(string colors) {
        int lens=colors.size();
        if(lens<3)
            return false;
        int num_a=0, num_b=0;
        for(int i=2;i<lens;i++)
        {
            if(colors[i]=='A'&&colors[i-1]=='A'&&colors[i-2]=='A')
                num_a++;
            if(colors[i]=='B'&&colors[i-1]=='B'&&colors[i-2]=='B')
                num_b++;
        }
        if(num_a>num_b)
            return true;
        else
            return false;
    }
};
