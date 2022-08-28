# 把A放在s最前面或把Z放在s最后面

s = 'AZAAAZ'

def oa1t27(s:str) -> int:
    sa, sz = 'A' + s, s + 'Z'

    def countAZ(s) -> int:
        l, r = 0, 0
        ans = 0
        ca = 0
        n = len(s)
        while r < n:
            if s[r] != 'Z':
                r += 1
            else:
                for i in range(l, r):
                    if s[i] == 'A':
                        ca += 1
                ans += ca
                l = r+1
                r += 1
        return ans
    return max(countAZ(sa), countAZ(sz))


print(oa1t27(s))


Deque<Integer> stack = new ArrayDeque<>();
        for(int i = 0; i <= arr.length; i++) {
            while(!stack.isEmpty() && (i == arr.length || arr[stack.peek()] > arr[i])) {
                int mid = stack.pop(), L = mid - (stack.isEmpty() ? -1 : stack.peek()), R = i - mid;
                res += (long) arr[mid] * L * R;
            }
            stack.push(i);
        }
        return (int) (res % 1_000_000_007);