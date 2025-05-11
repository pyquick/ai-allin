def correlation_coefficient(x, y):
    """
    计算两个变量的皮尔逊相关系数
    
    参数:
        x (list): 第一个变量数据集
        y (list): 第二个变量数据集
        
    返回:
        float: 相关系数，范围[-1,1]
    """
    if len(x) != len(y):
        raise ValueError("数据集长度必须相同")
    if len(x) < 2:
        raise ValueError("数据集长度至少为2")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(xi**2 for xi in x)
    sum_y_sq = sum(yi**2 for yi in y)
    sum_xy = sum(xi*yi for xi,yi in zip(x,y))
    
    numerator = sum_xy - (sum_x * sum_y)/n
    denominator_x = (sum_x_sq - sum_x**2/n)**0.5
    denominator_y = (sum_y_sq - sum_y**2/n)**0.5
    
    if denominator_x == 0 or denominator_y == 0:
        return 0
    
    return numerator / (denominator_x * denominator_y)