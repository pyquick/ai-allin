def chinese_remainder(n, a):
    """
    中国剩余定理求解
    
    参数:
        n (list): 模数列表
        a (list): 余数列表
        
    返回:
        int: 满足同余方程的最小正整数解
    """
    if len(n) != len(a):
        raise ValueError("模数和余数列表长度必须相同")
    
    total = 1
    for num in n:
        total *= num
    
    result = 0
    for ni, ai in zip(n, a):
        p = total // ni
        result += ai * modular_inverse(p, ni) * p
    
    return result % total

def modular_inverse(a, m):
    """
    计算模逆元
    
    参数:
        a (int): 整数
        m (int): 模数
        
    返回:
        int: a关于模m的逆元
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("逆元不存在")
    return x % m

def extended_gcd(a, b):
    """
    扩展欧几里得算法
    
    参数:
        a (int): 第一个数
        b (int): 第二个数
        
    返回:
        tuple: (gcd, x, y) 其中gcd是最大公约数，x和y满足ax + by = gcd
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)