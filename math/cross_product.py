def cross_product(a, b):
    """
    计算两个三维向量的叉积
    
    参数:
        a (list): 第一个三维向量
        b (list): 第二个三维向量
        
    返回:
        list: 叉积结果向量
    """
    if len(a) != 3 or len(b) != 3:
        raise ValueError("向量必须是三维的")
    
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]