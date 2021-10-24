class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t n2=0;
        cout<<"wai"<<n2<<endl;
        for(int i=0;i<32;i++)
        {
            n2*=2;
            cout<<i<<"-1:"<<n2<<endl;
            
            if(n%2==1)
              n2++;
            cout<<i<<"-2:"<<n2<<endl;    
            n/=2;
            cout<<i<<"-n:"<<n<<endl;
        }
        
        int ans=n2;
        return ans;
    }
};
