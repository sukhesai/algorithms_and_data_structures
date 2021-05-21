import math

def solution(l):
    pos1 = [None]*2 # contains least positions where l[i]%3 == 1 and 2
    pos2 = [None]*2 # contains second least positions where l[i]%3 == 1 and 2
    s = 0
    l.sort()
    for i, v in enumerate(l):
        s += v
        if v%3 == 1:
            if pos1[0] is None:
                pos1[0] = i
            elif pos2[0] is None:
                pos2[0] = i
        if v%3 == 2:
            if pos1[1] is None:
                pos1[1] = i
            elif pos2[1] is None:
                pos2[1] = i
    if s%3 == 0:
        return int(''.join(map(str,reversed(l))))
    elif s%3 == 1:
        if pos1[0] is not None:
            del l[pos1[0]]
            return int(''.join(map(str,reversed(l))))
        elif pos1[1] is not None and pos2[1] is not None:
            x = min(pos1[1],pos2[1])
            y = max(pos1[1],pos2[1])
            del l[y]
            del l[x]
            return int(''.join(map(str,reversed(l))))
        else:
            return 0
    elif s%3 == 2:
        if pos1[1] is not None:
            del l[pos1[1]]
            return int(''.join(map(str,reversed(l))))
        elif pos1[0] is not None and pos2[0] is not None:
            x = min(pos1[0],pos2[0])
            y = max(pos1[0],pos2[0])
            del l[y]
            del l[x]
            return int(''.join(map(str,reversed(l))))
        else:
            return 0


print(solution([1]))