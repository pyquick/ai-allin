def matrix_multiply(A, B):
    """
    计算两个矩阵的乘积
    
    参数:
        A (list of lists): 第一个矩阵
        B (list of lists): 第二个矩阵
        
    返回:
        list of lists: 矩阵乘积结果
    """
    if len(A[0]) != len(B):
        raise ValueError("矩阵A的列数必须等于矩阵B的行数")
    
    # 初始化结果矩阵
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    # 矩阵乘法
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result