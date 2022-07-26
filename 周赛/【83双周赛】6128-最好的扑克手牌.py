class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # count = 0
        if len(set(suits)) == 1: return "Flush"
        # ranks.sort()
        if len(set(ranks)) == 5: return "High Card"
        count = dict()
        for a in ranks:
            if a in count.keys():
                count[a] += 1
            else:
                count[a] = 1
        for a in count.keys():
            if count[a] >= 3:
                return "Three of a Kind"
        return "Pair"
