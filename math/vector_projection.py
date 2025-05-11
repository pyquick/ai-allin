def vector_projection(a, b):
    """
    计算向量a在向量b上的投影
    
    参数:
        a (list): 第一个向量
        b (list): 第二个向量
        
    返回:
        list: 投影向量
    """
    if len(a) != len(b):
        raise ValueError("向量长度必须相同")
    if not a or not b:
        raise ValueError("向量不能为空")
    
    dot_ab = sum(x*y for x,y in zip(a,b))
    dot_bb = sum(y*y for y in b)
    
    if dot_bb == 0:
        raise ValueError("向量b不能为零向量")
    
    scale = dot_ab / dot_bb
    return [scale * y for y in b]