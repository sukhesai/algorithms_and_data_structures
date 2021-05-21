def solution(g):
    rows, cols, ans = len(g), len(g[0]), 0
    previous = [[None]*(cols+1) for _ in range(rows+1)]
    true_config = ((True, False, False, False),
                   (False, True, False, False),
                   (False, False, True, False),
                   (False, False, False, True))
    dp = [[None]*(2**(rows+1)) for _ in range(cols+1)]  # stores number of possible ways for a given last column of previous config
    def find(r, c): # returns number of possible last state with the given privious state upto coordinate r,c-1
        if r == rows: # move to next column
            c += 1
            r = 0
        if c == cols: # all cells visited
            return 1
        ans  = 0
        if r == rows-1:
            multiset = 0
            for i in range(rows):
                if previous[i][c+1]:
                    multiset += (1 << i)
        if r == 0: # we are at the starting of some column > 0
            multiset = 0
            for i in range(rows+1):
                if previous[i][c]:
                    multiset += (1 << i)
            if dp[c][multiset] is not None:
                return dp[c][multiset]
            if g[r][c]:
                if (previous[0][c], previous[1][c]) == (True, True):
                    return 0
                elif (previous[0][c], previous[1][c]) == (False, False):
                    for config in ((True, False),(False, True)):
                        previous[0][c+1], previous[1][c+1] = config
                        ans += find(r+1, c)
                else:
                    previous[0][c+1], previous[1][c+1] = False, False
                    ans += find(r+1, c)
            else:
                if (previous[0][c], previous[1][c]) == (True, True):
                    for config in ((True, False),(False, True),(True,True),(False,False)):
                        previous[0][c+1], previous[1][c+1] = config
                        ans += find(r+1, c)
                elif (previous[0][c], previous[1][c]) == (False, False):
                    for config in ((True,True),(False,False)):
                        previous[0][c+1], previous[1][c+1] = config
                        ans += find(r+1, c)
                else:
                    for config in ((True,True),(True,False),(False,True)):
                        previous[0][c+1], previous[1][c+1] = config
                        ans += find(r+1, c)
        elif c == 0: # we are examining first column
            if g[r][c]:
                if (previous[r][0], previous[r][1]) == (True, True):
                    return 0
                elif (previous[r][0], previous[r][1]) == (False, False):
                    for config in ((True,False),(False,True)):
                        previous[r+1][0], previous[r+1][1] = config
                        x = find(r+1, c)
                        if r == rows-1:
                            n_multiset = multiset
                            if previous[r+1][1]:
                                n_multiset += (1 << rows)
                            dp[1][n_multiset] = x
                        ans += x
                else:
                    previous[r+1][0], previous[r+1][1] = False, False
                    x = find(r+1, c)
                    if r == rows-1:
                        n_multiset = multiset
                        if previous[r+1][1]:
                            n_multiset += (1 << rows)
                        dp[1][n_multiset] = x
                    ans += x
            else:
                if (previous[r][0], previous[r][1]) == (True, True):
                    for config in ((True, False),(False, True),(True,True),(False,False)):
                        previous[r+1][0], previous[r+1][1] = config
                        x = find(r+1, c)
                        if r == rows-1:
                            n_multiset = multiset
                            if previous[r+1][1]:
                                n_multiset += (1 << rows)
                            dp[1][n_multiset] = x
                        ans += x
                elif (previous[r][0], previous[r][1]) == (False, False):
                    for config in ((True,True),(False,False)):
                        previous[r+1][0], previous[r+1][1] = config
                        x = find(r+1, c)
                        if r == rows-1:
                            n_multiset = multiset
                            if previous[r+1][1]:
                                n_multiset += (1 << rows)
                            dp[1][n_multiset] = x
                        ans += x
                else:
                    for config in ((True, False),(False, True),(True,True)):
                        previous[r+1][0], previous[r+1][1] = config
                        x = find(r+1, c)
                        if r == rows-1:
                            n_multiset = multiset
                            if previous[r+1][1]:
                                n_multiset += (1 << rows)
                            dp[1][n_multiset] = x
                        ans += x
        else:
            if g[r][c]:
                if (previous[r][c], previous[r+1][c], previous[r][c+1]) == (False, False, False):
                    previous[r+1][c+1] = True
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset+(1 << rows)] = x
                    ans += x
                elif (previous[r][c], previous[r+1][c], previous[r][c+1]) in ((True, False, False),(False, True, False),(False, False, True)):
                    previous[r+1][c+1] = False
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset] = x
                    ans += x
                else:
                    return 0
            else:
                if (previous[r][c], previous[r+1][c], previous[r][c+1]) == (False, False, False):
                    previous[r+1][c+1] = False
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset] = x
                    ans += x
                elif (previous[r][c], previous[r+1][c], previous[r][c+1]) in ((True, False, False),(False, True, False),(False, False, True)):
                    previous[r+1][c+1] = True
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset+(1 << rows)] = x
                    ans += x
                else:
                    previous[r+1][c+1] = True
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset+(1 << rows)] = x
                    ans += x
                    previous[r+1][c+1] = False
                    x = find(r+1, c)
                    if r == rows-1:
                        dp[c+1][multiset] = x
                    ans += x
        return ans
    
    if g[0][0]:
        for config in true_config:
            previous[0][0],previous[0][1],previous[1][0],previous[1][1] = config
            ans += find(1,0)
        return ans
    for i1 in (True, False):
        for i2 in (True, False):
            for i3 in (True, False):
                for i4 in (True, False):
                    if (i1,i2,i3,i4) not in true_config:
                        previous[0][0],previous[0][1],previous[1][0],previous[1][1] = i1,i2,i3,i4
                        ans += find(1,0)
    return ans


g = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]
print(solution(g))