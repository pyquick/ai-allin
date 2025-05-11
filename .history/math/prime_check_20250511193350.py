def is_prime(n):
    """
    检测一个数是否为素数
    
    参数:
        n (int): 待检测的正整数
        
    返回:
        bool: 如果是素数返回True，否则返回False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True