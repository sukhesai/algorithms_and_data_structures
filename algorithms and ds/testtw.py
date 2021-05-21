
def solve(deadlines, credits, durations):
    if len(deadlines) == 0:
        return 0
    zipped = list(zip(deadlines,credits,durations))
    zipped.sort(key=lambda x: x[0])
    [deadlines,credits,durations] = list(zip(*zipped))
    print(deadlines)
    print(credits)
    print(durations)
    dp = [[None]*(len(deadlines)) for _ in range(max(deadlines)+2)] # dp[i][j] is max credit for
                                                                # before day i and at most j assignments
    result = [[None]*(len(deadlines)) for _ in range(max(deadlines)+2)]
    def find(d,i):
        print(f'entered find({d},{i})')
        if i < 0 or d <= 0:
            print(f'returned find({d},{i})=0')
            return 0
        if dp[d][i] is None:
            if durations[i] <= d and min(deadlines[i],d-1)-durations[i]+1>=0:
                print(f'{i}th assignment can be taken')
                print(f'cost if {i}th  taken = {find(min(deadlines[i],d-1)-durations[i]+1,i-1)+credits[i]}')
                print(f'cost if {i}th not taken = {find(d,i-1)}')
                if find(min(deadlines[i],d-1)-durations[i]+1,i-1)+credits[i] > find(d,i-1):
                    result[d][i] = 1
                    dp[d][i] = find(min(deadlines[i],d-1)-durations[i]+1,i-1)+credits[i]
                else:
                    result[d][i] = 0
                    dp[d][i] = find(d,i-1)
            else:
                print(f'{i}th assignment can not be taken')
                result[d][i] = 0
                dp[d][i] = find(d,i-1)
        print(f'returned find({d},{i})={dp[d][i]}')
        return dp[d][i]
    x = find(max(deadlines)+1,len(deadlines)-1)
    def print_result(d,i):
        if i<0 or d <=0:
            print(f'finished as i={i} and d={d}')
            return
        #print(d,i)
        if result[d][i] is None:
            print('Impossible here')
        if result[d][i] == 0:
            print(f'{i}th not taken')
            print_result(d,i-1)
        print(f'{i}th taken')
        print_result(d-durations[i],i-1)
    print_result(max(deadlines)+1,len(deadlines)-1)
    return x

deadlines = [85, 75, 97, 171, 67, 106, 54, 129, 81, 196]
credits = [59, 13, 43, 80, 81, 83, 5, 45, 86, 29]
durations = [83, 9, 31, 64, 93, 5, 12, 100, 48, 75]
print(solve(deadlines,credits,durations))