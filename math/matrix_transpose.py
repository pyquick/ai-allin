def matrix_transpose(matrix):
    """
    计算矩阵的转置
    
    参数:
        matrix (list of lists): 输入矩阵
        
    返回:
        list of lists: 转置后的矩阵
    """
    if not matrix or not matrix[0]:
        return []
    
    # 使用列表推导式实现转置
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]