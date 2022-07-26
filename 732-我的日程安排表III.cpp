class MyCalendarThree {
    // 尝试用C++完成插旗法
public:
    map<int, int> time;
    MyCalendarThree() {

    }
    
    int book(int start, int end) {
        
        time[start] += 1, time[end] -= 1;
        int cur=0, ans=0;
        for(auto& a:time)
        {
            cur += a.second;
            ans=max(cur, ans);
        }
        
        return ans;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
