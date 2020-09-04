def rotate(matrix):
    # code here
    n = len(matrix)
    if n < 3:
        i = 0
        j = 0
        t = matrix[i][j]
        matrix[i][j] = matrix[j][n-1-i]
        matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
        matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
        matrix[n-1-j][i] = t
    else:
        for i in range((n-1)//2):
            step = n-1-2*i
            for j in range(i, i+step):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = t
