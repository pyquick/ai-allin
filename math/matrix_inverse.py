def matrix_inverse(matrix):
    """
    计算方阵的逆矩阵
    
    参数:
        matrix (list of lists): 可逆方阵
        
    返回:
        list of lists: 逆矩阵
    """
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("输入必须是一个方阵")
    
    n = len(matrix)
    det = matrix_determinant(matrix)
    if det == 0:
        raise ValueError("矩阵不可逆，行列式为0")
    
    # 计算伴随矩阵
    adjoint = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 计算余子式
            minor = [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
            # (-1)^(i+j) * 余子式的行列式
            adjoint[j][i] = ((-1)**(i+j)) * matrix_determinant(minor)
    
    # 计算逆矩阵 = 伴随矩阵 / 行列式
    return [[adjoint[i][j]/det for j in range(n)] for i in range(n)]