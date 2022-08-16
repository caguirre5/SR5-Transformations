import math as m


def MultiplyMatrix(M1, M2):
    matrix = []
    for i in range(len(M1)):
        matrix.append([])
        for j in range(len(M2[0])):
            matrix[i].append(0)

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M1[0])):
                matrix[i][j] += M1[i][k] * M2[k][j]
    return matrix


def IdentityOp(a):
    matrix = []
    for i in range(0, a):
        matrix.append([])
        for j in range(0, a):
            if (i == j):
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix


def MV(M, V):
    matriz = []
    for fila in M:
        res = 0
        for col in range(len(fila)):
            res += (fila[col]*V[col])
        matriz.append(res)
    return matriz


def Cross(A, B):
    R = []
    R.append(A[1]*B[2] - A[2]*B[1])
    R.append(A[2]*B[0] - A[0]*B[2])
    R.append(A[0]*B[1] - A[1]*B[0])
    return R


def Substract(A, B):
    R = []
    for i in range(len(A)):
        R.append(A[i] - B[i])
    return R


def Normalize(V):
    L = m.sqrt(V[0]**2 + V[1]**2 + V[2]**2)
    VN = [
        V[0]/L, V[1]/L, V[2]/L
    ]
    return VN


def Dot(A, B):
    return sum([x*y for x, y in zip(A, B)])


def MatrizCof(M):
    Matrix = [
        [
            ((M[1][1]*M[2][2])-(M[2][1]*M[1][2])),
            -((M[1][0]*M[2][2])-(M[2][0]*M[1][2])),
            ((M[1][0]*M[2][1])-(M[2][0]*M[1][1]))
        ],
        [
            -((M[0][1]*M[2][2])-(M[2][1]*M[0][2])),
            ((M[0][0]*M[2][2])-(M[2][0]*M[0][2])),
            -((M[0][0]*M[2][1])-(M[2][0]*M[0][1]))
        ],
        [
            ((M[0][1]*M[1][2])-(M[1][1]*M[0][2])),
            -((M[0][0]*M[1][2])-(M[1][0]*M[0][2])),
            ((M[0][0]*M[1][1])-(M[1][0]*M[0][1]))
        ]
    ]
    return Matrix


def MatrizTra(M):
    Temp = [[] for i in M[0]]
    for i in range(len(M)):
        for j in range(len(M[i])):
            Temp[i].append(M[j][i])
    return Temp


def MatrizAdj(M):
    Matrix = MatrizCof(M)
    MatrixAdj = MatrizTra(Matrix)
    return MatrixAdj


def MatrixDet(M):
    Determinante = M[0][0]*((M[1][1]*M[2][2]) - (M[2][1]*M[1][2]))-M[0][1]*(
        (M[1][0]*M[2][2])-(M[2][0]*M[1][2]))+M[0][2]*((M[1][0]*M[2][1])-(M[2][0]*M[1][1]))
    return Determinante


def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]


def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a


def subtractArrays(A, B):
    dims = isinstance(A, list) + 2 * isinstance(B, list)
    if dims == 3:
        return [subtractArrays(ra, rb) for ra, rb in zip(A, B)]
    if dims == 2:
        return [subtractArrays(A, rb) for rb in B]
    if dims == 1:
        return [subtractArrays(ra, B) for ra in A]
    return A-B


def crossProduct(A, B):
    Res = [A[1]*B[2] - A[2]*B[1],
           A[2]*B[0] - A[0]*B[2],
           A[0]*B[1] - A[1]*B[0]]

    return Res


def norm(list):
    dist = m.sqrt(((list[0] - list[1]) ** 2)
                  + ((list[1] - list[2]) ** 2)
                  + ((list[2] - list[0]) ** 2))

    return dist


def MatrixInv(a):
    tmp = [[] for _ in a]
    for i, row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret
