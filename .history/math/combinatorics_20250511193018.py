def combination(n, k):
    """
    计算组合数C(n,k)
    
    参数:
        n (int): 总数
        k (int): 选取数
        
    返回:
        int: 组合数C(n,k)
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid input: n and k must be non-negative and k <= n")
    if k == 0 or k == n:
        return 1
    
    # 使用组合数性质C(n,k)=C(n,n-k)减少计算量
    if k > n - k:
        k = n - k
    
    result = 1
    for i in range(1, k+1):
        result = result * (n - k + i) // i
    return result

def permutation(n, k):
    """
    计算排列数P(n,k)
    
    参数:
        n (int): 总数
        k (int): 选取数
        
    返回:
        int: 排列数P(n,k)
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid input: n and k must be non-negative and k <= n")
    
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result