def euler_totient(n):
    """
    计算欧拉函数φ(n)，即小于n且与n互质的正整数的个数
    
    参数:
        n (int): 正整数
        
    返回:
        int: 欧拉函数值
    """
    if n <= 0:
        raise ValueError("输入必须为正整数")
    
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result