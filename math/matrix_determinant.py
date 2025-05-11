def matrix_determinant(matrix):
    """
    计算方阵的行列式
    
    参数:
        matrix (list of lists): 方阵
        
    返回:
        float: 行列式值
    """
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("输入必须是一个方阵")
    
    n = len(matrix)
    
    # 1x1矩阵直接返回元素
    if n == 1:
        return matrix[0][0]
    
    # 2x2矩阵直接计算
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(n):
        # 计算余子式
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # 递归计算行列式
        det += ((-1) ** col) * matrix[0][col] * matrix_determinant(minor)
    
    return det