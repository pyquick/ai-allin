def modular_exponentiation(base, exponent, modulus):
    """
    快速模幂算法计算(base^exponent) % modulus
    
    参数:
        base (int): 底数
        exponent (int): 指数
        modulus (int): 模数
        
    返回:
        int: (base^exponent) % modulus
    """
    if modulus == 1:
        return 0
    if exponent < 0:
        raise ValueError("指数必须为非负整数")
    
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result