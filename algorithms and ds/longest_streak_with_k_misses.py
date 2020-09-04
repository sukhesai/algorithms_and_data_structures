from collections import deque


def solve(s, k):
    n = len(s)
    dq = deque()
    max_streak = 0
    left_misses = k
    curr_streak = 0
    for i in range(n):
        if s[i] == 'w':
            if left_misses < 1:
                if dq:
                    curr_streak = i - dq.popleft()
                    dq.append(i)
                else:
                    curr_streak = 0
            else:
                curr_streak += 1
                left_misses -= 1
                dq.append(i)
        else:
            curr_streak += 1
        max_streak = max(max_streak, curr_streak)
    return max_streak


s = 'wbbbwbwwwb'
print(solve(s, 2))
