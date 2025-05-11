def gcd(a, b):
    """
    计算两个数的最大公约数(GCD)
    
    参数:
        a (int): 第一个整数
        b (int): 第二个整数
        
    返回:
        int: a和b的最大公约数
    """
    while b:
        a, b = b, a % b
    return a