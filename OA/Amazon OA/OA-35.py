from typing import List

memory = [1,4,4,6,9,4]
k = 2

def oa1t35(memory: List[int], k: int) -> int:
    sum_memory = sum(memory)
    subsum, pre = sum(memory[0:k]), sum(memory[0:k])
    n = len(memory)
    for i in range(0,n-k):
        pre += (memory[i+k]-memory[i])
        subsum = max(subsum, pre)
    return sum_memory-subsum

print(oa1t35(memory, k))