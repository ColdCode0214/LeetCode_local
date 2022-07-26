class NumberContainers {
    map<int, int> i2n;
    map<int, set<int>> n2i;
public:
    NumberContainers() {

    }
    
    void change(int index, int number) {
        if(i2n.count(index))
        {
            int pre=i2n[index];
            n2i[pre].erase(index);
        }
        i2n[index]=number;
        n2i[number].insert(index);
    }
    
    int find(int number) {
        set<int> &st=n2i[number];
        if(st.size()==0)
            return -1;
        return *(st.begin());
    }
};

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
