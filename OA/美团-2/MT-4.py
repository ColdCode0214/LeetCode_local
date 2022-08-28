import heapq

n, m = input().split()
n = int(n)  # A的长度
m = int(m)  # B的长度
temp = input("")
a = [int(x) for x in temp.split()]
temp = input("")
b = [int(x) for x in temp.split()]
ans = 0
diff = abs(n - m)
base = 0
arr = list()
if n >= m:  # A比B长
    cp = a
    heapq.heapify(cp)
    for i in range(diff):
        temp = heapq.heappop(cp)
        base += temp
        arr.append(temp)
    flag = [0] * diff  # 标记都有哪些多余的数已经被抛弃过
    ia, ib = 0, 0
    while ia < n and ib < m:
        if a[ia] in arr:
            find = 0
            for j in range(diff):
                if arr[j] == a[ia] and flag[ia] == 0:
                    flag[ia] = 1
                    find = 1
                    break
            if find == 1:
                ia += 1
            else:
                ans += abs(b[ib] - a[ia])
                ia += 1
                ib += 1
        else:
            ans += abs(b[ib] - a[ia])
            ia += 1
            ib += 1
    print(ans)

else:  # m >= n B比A长
    cp = b
    heapq.heapify(cp)
    for i in range(diff):
        temp = heapq.heappop(cp)
        base += temp
        arr.append(temp)
    flag = [0] * diff  # 标记都有哪些多余的数已经被抛弃过
    ia, ib = 0, 0
    while ia < n and ib < m:
        if b[ib] in arr:
            find = 0
            for j in range(diff):
                if arr[j] == b[ib] and flag[ib] == 0:
                    flag[ib] = 1
                    find = 1
                    break
            if find == 1:
                ib += 1
            else:
                ans += abs(b[ib] - a[ia])
                ib += 1
                ia += 1

        else:
            ans += abs(b[ib] - a[ia])
            ia += 1
            ib += 1
    print(ans)

