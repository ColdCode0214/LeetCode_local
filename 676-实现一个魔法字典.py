class MagicDictionary:

    def __init__(self):
        self.mp = list()


    def buildDict(self, dictionary: List[str]) -> None:
        for a in dictionary:
            self.mp.append(a)

    def search(self, searchWord: str) -> bool:
        for a in self.mp:
            print(type(a))
            if len(a) == len(searchWord):
                n = len(a)
                count = 0
                for i in range(n):
                    if a[i] != searchWord[i]:
                        count += 1
                if count == 1: return True
        return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)