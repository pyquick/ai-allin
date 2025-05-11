def factorial(n):
    """
    计算n的阶乘
    
    参数:
        n (int): 非负整数
        
    返回:
        int: n的阶乘
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    return result