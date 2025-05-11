def median(data):
    """
    计算数据集的中位数
    
    参数:
        data (list): 数值数据集
        
    返回:
        float: 中位数
    """
    if not data:
        raise ValueError("数据集不能为空")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        return sorted_data[n//2]
    else:
        return (sorted_data[n//2-1] + sorted_data[n//2]) / 2