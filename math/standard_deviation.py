def standard_deviation(data):
    """
    计算数据集的标准差
    
    参数:
        data (list): 数值数据集
        
    返回:
        float: 标准差
    """
    if not data:
        raise ValueError("数据集不能为空")
    
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    return variance ** 0.5