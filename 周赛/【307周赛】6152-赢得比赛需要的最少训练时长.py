class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        n = len(energy)  # 对手总人数
        energy_sum = sum(energy)
        ans = 0
        if energy_sum >= initialEnergy:
            ans += energy_sum + 1 - initialEnergy
        # print(ans)
        curE = initialExperience
        for i in range(n):
            if experience[i] >= curE:
                ans += experience[i] - curE + 1
                curE = experience[i] + 1
            curE += experience[i]
        return ans
