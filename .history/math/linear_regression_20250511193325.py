def linear_regression(x, y):
    """
    简单线性回归计算
    
    参数:
        x (list): 自变量数据集
        y (list): 因变量数据集
        
    返回:
        tuple: (斜率, 截距)
    """
    if len(x) != len(y):
        raise ValueError("x和y的长度必须相同")
    if len(x) < 2:
        raise ValueError("数据集长度至少为2")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(xi**2 for xi in x)
    sum_xy = sum(xi*yi for xi,yi in zip(x,y))
    
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n
    
    return (slope, intercept)