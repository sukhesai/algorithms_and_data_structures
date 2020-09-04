#code


if __name__ == '__main__':

    i = int(input())
    for _ in range(i):
        n = int(input())
        arr = list(map(int, input().split()))
        start_end = arr[0]
        max_reach = 0
        jumps = 1
        if arr[0] >= n-1:
            print(1)
        else:
            for i in range(n):
                print('start',i,max_reach)
                if i > max_reach:
                    print(-1)
                    break
                max_reach = max(max_reach, i+arr[i])
                if max_reach >= n-1:
                    print(jumps+1)
                    break
                if i == start_end:
                    start_end = max_reach
                    jumps += 1
                print(i, max_reach)
