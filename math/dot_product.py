def dot_product(a, b):
    """
    计算两个向量的点积
    
    参数:
        a (list): 第一个向量
        b (list): 第二个向量
        
    返回:
        float: 点积结果
    """
    if len(a) != len(b):
        raise ValueError("向量长度必须相同")
    
    return sum(x * y for x, y in zip(a, b))