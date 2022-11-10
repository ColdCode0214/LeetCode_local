class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        np, nt = len(players), len(trainers)
        players.sort()
        trainers.sort()
        ans = 0
        ti = 0
        stop = 0
        for i in range(np):
            while ti < nt and trainers[ti] < players[i]:
                ti += 1
            if ti == nt:
                break
            if trainers[ti] >= players[i]:
                ans += 1
                ti += 1
            if ti == nt:
                break
        return ans
