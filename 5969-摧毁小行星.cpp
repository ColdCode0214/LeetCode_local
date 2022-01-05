class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        int lens=asteroids.size();
        long long int w=mass;
        sort(asteroids.begin(), asteroids.end());
        for(int i=0;i<lens;i++)
        {
            if(w>=asteroids[i])
                w+=asteroids[i];
            else
                return false;
        }
        return true;
    }
};
