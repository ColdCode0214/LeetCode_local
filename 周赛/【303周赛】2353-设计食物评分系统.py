from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # 存储由food到cuisines和rating的映射，是一对一关系
        self.f2cr = dict() 
        # 存储由cuisines到food和rating的映射，是一对多关系
        self.c2rf = dict() # 因为答案会取先按rating排名后按食物名称字典序排名，因此该dict在存储时要先存rating，后存food
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.f2cr[food] = [cuisine, rating]
            if cuisine not in self.c2rf:
                self.c2rf[cuisine] = SortedList()
            self.c2rf[cuisine].add([-rating, food]) # rating取负存储可使大值排在前面

    def changeRating(self, food: str, newRating: int) -> None:
        preRate = self.f2cr[food][1]
        cuisine = self.f2cr[food][0]
        if preRate == newRating: return
        else:
            # 新分数与历史分数不等的情况下，需要删除cuisines映射中的原数据，两次更新将在if外再执行
            self.c2rf[cuisine].remove([-preRate, food])
            self.f2cr[food][1] = newRating
            self.c2rf[cuisine].add([-newRating, food])


    def highestRated(self, cuisine: str) -> str:
        return self.c2rf[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)