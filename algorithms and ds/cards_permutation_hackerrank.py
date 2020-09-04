

class fenwick:
    def __init__(self, n):
        self.tree = [0]*(n+1)

    def update(self, i):
        # i is 0 based index
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & (-i)

    def query(self, i):
        # i is 0 based index
        sum = 0
        i += 1
        while i > 0:
            sum += self.tree[i]
            i -= i & (-i)
        return sum


def solve(x):
    n = len(x)
    mod = 1000000007
    missing = [True]*n
    bit1 = fenwick(n)
    bit2 = fenwick(n)
    for i in range(n):
        x[i] -= 1
        if x[i] != -1:
            missing[x[i]] = False
    missisng_elems = []
    for i in range(n):
        if missing[i]:
            missisng_elems.append(i)
    missing_sum = 0
    m = len(missisng_elems)
    for i in missisng_elems:
        missing_sum += i
        if i < n-1:
            bit2.update(i+1)
    fact = [1]*500010
    for i in range(1, 500010):
        fact[i] = i*fact[i-1] % mod
    total_cost = 0
    p = 0
    y = 0
    print('bit1:')
    for i in range(n):
        print(bit1.query(i))
    print('bit2:')
    for i in range(n):
        print(bit2.query(i))
    print('missing array:', missisng_elems)
    for i in range(n-1):
        if x[i] != -1:
            if m == 0:
                D1 = bit1.query(x[i])
                bit1.update(x[i]+1)
                cost = (x[i] - D1)*fact[n-i-1]
            else:
                D1 = bit1.query(x[i])*m
                no_of_smaller_missing_elems = bit2.query(x[i])
                D2 = no_of_smaller_missing_elems*p
                print('case1 i:{} x[i]:{} no_of_smaller_missing_elems:{} p:{} m:{} no_of_smaal_present_elems:{}'.format(i, x[i], no_of_smaller_missing_elems, p, m, bit1.query(x[i])))
                print('D1:{} D2:{}'.format(D1, D2))
                print('updating bit1 at {}'.format(x[i]+1))
                bit1.update(x[i]+1)
                print('updated bit1 :')
                for l in range(n):
                    print(bit1.query(l))
                cost = (x[i]*m - (D1 + D2))*fact[m-1]*fact[n-i-1]
                y += m - no_of_smaller_missing_elems
                print('i:{}, x[i]:{}, cost:{}'.format(i, x[i], cost))
                total_cost += cost % mod
        else:
            if p == 0:
                print('case2 y:{} '.format(y))
                cost = (missing_sum - y)*fact[m-1]*fact[n-i-1]
                print('i:{}, x[i]:{}, cost:{}'.format(i, x[i], cost))
                total_cost += cost % mod
            else:
                D1 = p*m*(m-1)//2
                D2 = y*(m-1)
                print('case3 D1:{} D2:{}'.format(D1, D2))
                cost = (missing_sum * (m-1) - (D1 + D2))*fact[m-2]*fact[n-i-1]
                print('i:{}, x[i]:{}, cost:{}'.format(i, x[i], cost))
                total_cost += cost % mod
            p += 1
        print('i:{} toatalcost:{}'.format(i, total_cost))
    return (total_cost + fact[m]) % mod


a = list(map(int, "0 2 3 0".split()))
print(solve(a))
