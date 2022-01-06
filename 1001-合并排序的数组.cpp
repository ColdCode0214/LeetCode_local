class Solution {
public:
    void merge(vector<int>& A, int m, vector<int>& B, int n) {
        int p1=m-1, p2=n-1;
        int index=m+n-1;
        while(p1>=0 && p2>=0)
        {
            if(A[p1]>B[p2])
            {
                A[index]=A[p1];
                p1--;
            }
            else
            {
                A[index]=B[p2];
                p2--;
            }
            index--;
        }
        while(p1>=0)
        {
            A[index]=A[p1];
            p1--;
            index--;
        }
        while(p2>=0)
        {
            A[index]=B[p2];
            p2--;
            index--;
        }
        return;
    }
};
