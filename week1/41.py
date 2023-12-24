N, B = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

def mul_mat(mat1, mat2):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += mat1[i][k] * mat2[k][j]
                # (0,0) += (0,0)*(0,0) + (0,1)*(1,0)
                # (0,1) += (0,0)*(0,1) + (0,1)*(1,1)
                # (1,0) += (1,0)*(0,0) + (1,1)*(1,0)
    
    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000
            
    return result

def exp_mat(mat, exp):
    if exp == 1:
        for i in range(len(mat)):
            for j in range(len(mat)):
                mat[i][j] %= 1000
        return mat
    
    if exp % 2 == 0:
        newmat = exp_mat(mat, exp // 2)
        return mul_mat(newmat, newmat)
    else:
        newmat = exp_mat(mat, exp // 2)
        return mul_mat(mul_mat(newmat, newmat), mat)

res = exp_mat(mat, B)

for i in range(N):
    for j in range(N):
        print(res[i][j], end= ' ')
    print()