import math
def vector_angle(a, b):
    """
    计算两个向量之间的夹角(弧度)
    
    参数:
        a (list): 第一个向量
        b (list): 第二个向量
        
    返回:
        float: 夹角(弧度)
    """
    if len(a) != len(b):
        raise ValueError("向量长度必须相同")
    if not a or not b:
        raise ValueError("向量不能为空")
    
    dot = sum(x*y for x,y in zip(a,b))
    norm_a = sum(x**2 for x in a)**0.5
    norm_b = sum(x**2 for x in b)**0.5
    
    # 防止浮点误差导致acos参数超出[-1,1]范围
    cos_theta = dot / (norm_a * norm_b)
    cos_theta = max(-1.0, min(1.0, cos_theta))
    
    return math.acos(cos_theta)