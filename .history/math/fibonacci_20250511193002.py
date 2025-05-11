def fibonacci(n) ->:
    """
    计算第n个斐波那契数
    
    参数:
        n (int): 斐波那契数列的索引(从0开始)
        
    返回:
        int: 第n个斐波那契数
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b