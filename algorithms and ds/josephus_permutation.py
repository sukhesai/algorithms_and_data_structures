

def JosephusPermutation(n, m):
    a = [i+1 for i in range(n)]
    result = []
    lastrank = 1
    current_elements = n
    for _ in range(n):
        lastrank = (lastrank + m - 1) % current_elements
        if lastrank == 0:
            lastrank = current_elements
        result.append(a.pop(lastrank - 1))
        current_elements -= 1
    return result


res = JosephusPermutation(14, 3-1)
print(res)
