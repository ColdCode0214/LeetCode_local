class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        int lens=seats.size();
        sort(seats.begin(),seats.end());
        sort(students.begin(),students.end());
        int ans=0;
        for(int i=0;i<lens;i++)
            ans+=abs(seats[i]-students[i]);
        return ans;
    }
};
