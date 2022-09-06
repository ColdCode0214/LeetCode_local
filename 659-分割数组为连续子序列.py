class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        mp = dict()

        for i in range(n):
            if i == 0 or nums[i] - 1 not in mp:
                if nums[i] in mp:
                    heapq.heappush(mp[nums[i]], 1)
                else:
                    temp = list()
                    heapq.heapify(temp)
                    heapq.heappush(temp, 1)
                    mp[nums[i]] = temp
            else:
                if len(mp[nums[i] - 1]) == 0:
                    if nums[i] in mp:
                        heapq.heappush(mp[nums[i]], 1)
                    else:
                        temp = list()
                        heapq.heapify(temp)
                        heapq.heappush(temp, target)
                        mp[nums[i]] = temp
                else:
                    length = mp[nums[i] - 1]
                    target = heapq.heappop(length)
                    target += 1
                    if nums[i] in mp:
                        heapq.heappush(mp[nums[i]], target)
                    else:
                        temp = list()
                        heapq.heapify(temp)
                        heapq.heappush(temp, target)
                        mp[nums[i]] = temp
            # print("mp:", mp)
        for a in mp:
            if len(mp[a]) > 0 and mp[a][0] < 3:
                return False
        return True


