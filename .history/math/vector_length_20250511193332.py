def vector_length(vector):
    """
    计算向量的长度(模)
    
    参数:
        vector (list): 向量
        
    返回:
        float: 向量长度
    """
    if not vector:
        raise ValueError("向量不能为空")
    
    return sum(x**2 for x in vector)**0.5