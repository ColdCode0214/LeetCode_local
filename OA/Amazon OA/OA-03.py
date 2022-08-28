# 查找result的每一位是否在search中出现，当某一位没有出现时，从这一位开始往后的所有位就是要append的

searchWord = "armaze"
resultWord = "amazon"

def oa1t3(searchWord:str, resultWord:str) -> int:
    ns, nr = len(searchWord), len(resultWord)
    si, ri = 0, 0
    while si < ns and ri < nr:
        if searchWord[si] != resultWord[ri]:
            si += 1
        else:
            si += 1
            ri += 1
    return nr-ri

print(oa1t3(searchWord, resultWord))