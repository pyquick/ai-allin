def fast_power(base, power, mod=None):
    """
    快速幂算法计算base的power次方
    
    参数:
        base (int): 底数
        power (int): 指数
        mod (int, optional): 模数，如果提供则计算模幂
        
    返回:
        int: base^power 或 (base^power) % mod
    """
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = result * base
            if mod is not None:
                result %= mod
        base = base * base
        if mod is not None:
            base %= mod
        power = power // 2
    return result