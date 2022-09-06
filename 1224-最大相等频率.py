class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, sum_ = dict(), dict()
        max_ = 0
        ans = 0
        # cnt[i]=x表示数值i出现了x次；sum[i]=x表示出现了i次的数值有x个
        for i in range(n):
            if nums[i] in cnt:
                sum_[cnt[nums[i]]] -= 1 
                cnt[nums[i]] += 1
                if cnt[nums[i]] in sum_:
                    sum_[cnt[nums[i]]] += 1
                else:
                    sum_[cnt[nums[i]]] = 1
            else:
                cnt[nums[i]] = 1
                if cnt[nums[i]] in sum_:
                    sum_[cnt[nums[i]]] += 1
                else:
                    sum_[cnt[nums[i]]] = 1
            max_ = max(cnt[nums[i]], max_)
            if max_ == 1:
                ans = i+1
            elif max_ * sum_[max_] + 1 == i+1:
                ans = max_ * sum_[max_] + 1
            elif (max_ - 1) * (sum_[max_-1]+1) + 1 == i+1:
                ans = (max_ - 1) * (sum_[max_-1]+1) + 1
        return ans
