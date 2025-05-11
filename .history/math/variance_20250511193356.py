def variance(data):
    """
    计算数据集的方差
    
    参数:
        data (list): 数值数据集
        
    返回:
        float: 方差
    """
    if not data:
        raise ValueError("数据集不能为空")
    
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / n