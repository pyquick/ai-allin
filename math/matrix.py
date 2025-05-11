def matrix_multiply(a, b):
    """
    矩阵乘法
    
    参数:
        a (list): 二维矩阵
        b (list): 二维矩阵
        
    返回:
        list: 矩阵乘积
    """
    if len(a[0]) != len(b):
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix")
    
    # 初始化结果矩阵
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    
    # 矩阵乘法计算
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_transpose(matrix):
    """
    矩阵转置
    
    参数:
        matrix (list): 二维矩阵
        
    返回:
        list: 转置后的矩阵
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]