from tkinter.filedialog import askopenfiles


def matrixBlockSum(matrix, k):
    rows, cols = len(matrix), len(matrix[0])
    sumMat = [[0]* (cols + 1) for _ in range(rows + 1)]
    
    for r in range(rows):
        prefix = 0
        for c in range(cols):
            prefix += matrix[r][c]
            above = sumMat[r][c + 1]
            sumMat[r + 1][c + 1] = prefix + above
            
    ans = [[0]* cols for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            end_i = min(cols, i+k)
            end_j = min(rows, j+k)
            
            start_i = max(1, i-k)
            start_j = max(1, j-k)
            
            ans[i-1][j-1] = sumMat[end_i][end_j] - sumMat[start_i-1][end_j] -sumMat[end_i][start_j-1] + sumMat[start_i-1][start_j-1]
    return ans

print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
"""
 matrix rows: 3 cols: 3
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 | 
    
    end_i = min(3, 1+1)
    end_j = min(3, 1+1)
    
    start_i = max(1, 1-1)
    start_j = max(1, 1-1)
    
    ans[1-1][1-1] = sumMat[end_i 2][end_j 2] - sumMat[start_i-1 0][end_j 2] -sumMat[end_i 2][start_j-1 0] + sumMat[start_i-1 0][start_j-1 0]
                    = 12 - 0 - 0 + 0
    # 2D sumMat
      j:s              j:end
start i| 0 | 0  | 0  | 0  |
       | 0 | 1  | 3  | 6  |
       | 0 | 5  | 12 | 21 |
end i  | 0 | 12 | 27 | 45 |
"""