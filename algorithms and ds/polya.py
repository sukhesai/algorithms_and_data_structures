import math, collections
from fractions import gcd

def solution(w, h, s):
    # A symmetry is an operation by which an object can be shuffled without making it a different object.    
    # we have total (w!)(h!) number of symmetries in this counting problem 
    # as rows can be arranged in h! ways and columns in w! ways. Now we try to apply burnside's
    # lemma for counting total number of distinct objects given the set of all symmetries.
    # the formula says : total number of ways of coloring = (1/(no of symmetries))*(sigma(s**(no of cycles in each symmetry operation)))
    # where s is no of states. Now computing the number of cycles in each permutation(symmetry operation) is done as follow.
    # we iterate through the integer partitions of w.we know how many permutations of columns are of this type.
    # for each such type, we iterate through the partitions of number of rows. The number of cycles caused by n-length row-wise cycle
    # and m-length column-wise cycle is gcd(n,m) (it can be seen easily by calculating length of resulting orbits).This way
    # we can calculate the number of symmetris corresponding to the different number of cycles.
    if w < h:
        w, h = h, w
    # now generate integer partitons of w (which will also get us partitions of h)
    partition = {1: [[1]]}
    for i in range(2, w+1):
        ans = [[i]]
        for j in range(1, i):
            a = i-j
            for ptn in partition[j]:
                if ptn[0] <= a: # this condition eliminates duplicate partitions like [1,2] and [2,1]
                    ans.append([a]+ptn)
        partition[i] = ans
    def no_of_cycles(p1, p2):
        return sum([sum([gcd(i, j) for i in p1]) for j in p2])
    def no_of_permutations(n, typ):
        c = collections.Counter(typ)
        for i in c:
            n = n//((i**c[i])*(math.factorial(c[i])))
        return n
    fact_w, fact_h = math.factorial(w), math.factorial(h)
    no_of_perms = [0]*(h*w+1) # no_of_perms[i] = no of permutations having exactly i cycles
    for p1 in partition[w]:
        for p2 in partition[h]:
            no_of_perms[no_of_cycles(p1,p2)] += (no_of_permutations(fact_w,p1)*no_of_permutations(fact_h,p2))
    ans = 0
    pow_s = s
    for i in range(1,h*w+1):
        if no_of_perms[i]:
            ans += (pow_s*no_of_perms[i])
        pow_s *= s
    return str(ans//(fact_w*fact_h))


print(solution(2,2,2))