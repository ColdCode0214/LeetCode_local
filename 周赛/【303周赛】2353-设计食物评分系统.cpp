class FoodRatings {
    typedef pair<int, string> pis;
    map<string, pis> f2rc;
    map<string, set<pis>> c2rf;
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i=0;i<foods.size();i++)
        {
            f2rc[foods[i]]=pis(ratings[i],cuisines[i]);
            c2rf[cuisines[i]].insert(pis(-ratings[i],foods[i]));
        }
    }
    
    void changeRating(string food, int newRating) {
        pis &p=f2rc[food];
        c2rf[p.second].erase(pis(-p.first,food));
        p.first=newRating;
        c2rf[p.second].insert(pis(-newRating,food));
    }
    
    string highestRated(string cuisine) {
        return c2rf[cuisine].begin()->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
