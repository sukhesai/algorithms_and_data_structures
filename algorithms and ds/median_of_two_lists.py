
def median(a, b, n):
    if n == 1:
        return min(a[0], b[0])
    mid = (n-1)//2
    if a[mid] > b[mid]:
        return median(a[:mid+1], b[mid+1:], mid+1)
    else:
        return median(a[mid+1:], b[:mid+1], mid+1)


a = [1, 2, 2, 5, 7, 7, 9, 11]
b = [1, 3, 5, 6, 6, 7, 8, 10]
print(median(a, b, 8))
