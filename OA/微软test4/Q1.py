# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python (Python 3.6)
    if N > 0:
        flag = 1
    else:
        flag = -1
        N = -N
    arr = list()
    cp = N
    lens = 0  # 表示N的位数，即arr的长度
    while cp > 0:
        arr.append(cp % 10)
        cp = int(cp / 10)
        lens += 1
    arr.reverse()
    index = list()
    count = 0  # 表示N中有5的数量,即index的长度
    for i in range(lens):
        if arr[i] == 5:
            index.append(i)
            count += 1
    k = -1
    if flag == 1:
        for i in range(count):
            if i < count - 1:
                if arr[index[i] + 1] > 5:
                    k = index[i]
                    break
            else:
                k = index[i]
    else:
        for i in range(count):
            if i < count - 1:
                if arr[index[i] + 1] < 5:
                    k = index[i]
                    break
            else:
                k = index[i]
    temp = arr[0:k]
    temp.extend(arr[k + 1:])
    ans = 0
    for i in range(lens - 1):
        ans *= 10
        ans += temp[i]
    return flag * ans
    pass
    '''
    ans, temp = list(), list()
    for i in range(count):
        temp = arr[0:index[i]]
        temp.extend(arr[index[i]+1:])
        ans.append(temp)
    # print(ans) # ans行数为count，列数为lens-1
    max_, k, num, min_ = -1, -1, 0, 10
    if flag == 1:
        for j in range(lens-1):
            max_, k, num = -1, -1, 0
            for i in range(count):
                if ans[i][j] > max_:
                    max_ = ans[i][j]
                    num = 1
                    k = i
                elif ans[i][j] == max_:
                    num += 1
            if num == 1:
                break
        res = 0
        for i in range(lens-1):
            res *= 10
            res += ans[k][i]
        return res
    else:
        for j in range(lens-1):
            min_, k, num = 10, -1, 0
            for i in range(count):
                if ans[i][j] < min_:
                    min_ = ans[i][j]
                    num = 1
                    k = i
                elif ans[i][j] == min_:
                    num += 1
            if num == 1:
                break
        res = 0
        for i in range(lens-1):
            res *= 10
            res += ans[k][i]
        return -res
    '''

