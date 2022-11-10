class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(ids)
        degree = dict()
        record = dict()
        max_ = dict()
        # for name in creators:
        for i in range(n):
            name = creators[i]
            if name in degree:
                degree[name] += views[i]
                if views[i] > max_[name]:
                    record[name] = ids[i]
                    max_[name] = views[i]
                elif views[i] == max_[name]:
                    if ids[i] < record[name]:
                        record[name] = ids[i]
            else:
                degree[name] = views[i]  # 更新某作者的流行度
                record[name] = ids[i]  # 更新该作者最流行作品的ID
                max_[name] = views[i]  # 记录该作者最流行作品的播放量
        highest = max(degree.values())
        ans = list()
        for a in degree:
            if degree[a] == highest:
                ans.append([a, record[a]])
        return ans
