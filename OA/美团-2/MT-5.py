n, m = input().split()
n = int(n)
m = int(m)
temp = input("")
b = [int(x) for x in temp.split()]  # n个磨损，第i个需bi重的物品
temp = input("")
a = [int(x) for x in temp.split()]  # m种材料，第i种重ai
a.sort()
b.sort()
pre = 0
if b[n - 1] > a[m - 1]:
    print(-1)
else:
    l, r = 0, m - 1  # 代表查找物品的下标
    ans = 0
    for i in range(n):
        for j in range(pre, m):
            if a[j] >= b[i]:
                ans += a[j]
                pre = j
                break
    print(ans)
    # while l <= r:
    #     print("l:", l, "r:", r)
    #     mid = int((l+r)/2)
    #     print("mid:", mid)
    #     if a[mid] == b[i]:
    #         ans += b[i]
    #         l = mid
    #     elif a[mid] < b[i]:
    #         l = mid
    #     else: # a[mid] > b[i]
    #         if mid == 0 or a[mid-1] < b[i]:
    #             ans += a[mid]
    #             break
    #         else:
    #             r = mid-1

