def matrix_eigenvalues(matrix, max_iterations=1000, tolerance=1e-10):
    """
    计算实对称矩阵的特征值(使用QR算法)
    
    参数:
        matrix (list of lists): 实对称矩阵
        max_iterations (int): 最大迭代次数
        tolerance (float): 收敛容差
        
    返回:
        list: 特征值列表
    """
    if not matrix or len(matrix) != len(matrix[0]):
        raise ValueError("输入必须是一个方阵")
    
    n = len(matrix)
    A = [row[:] for row in matrix]  # 创建矩阵副本
    
    for _ in range(max_iterations):
        # QR分解
        Q = [[0.0]*n for _ in range(n)]
        R = [[0.0]*n for _ in range(n)]
        
        # Gram-Schmidt正交化
        for j in range(n):
            v = [A[i][j] for i in range(n)]
            for k in range(j):
                r = sum(Q[i][k] * A[i][j] for i in range(n))
                R[k][j] = r
                for i in range(n):
                    v[i] -= r * Q[i][k]
            norm = sum(x**2 for x in v)**0.5
            R[j][j] = norm
            for i in range(n):
                Q[i][j] = v[i] / norm if norm != 0 else 0
        
        # 计算新的A = RQ
        A = [[0.0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    A[i][j] += R[i][k] * Q[k][j]
        
        # 检查是否收敛(下三角元素接近0)
        converged = True
        for i in range(1, n):
            for j in range(i):
                if abs(A[i][j]) > tolerance:
                    converged = False
                    break
            if not converged:
                break
        if converged:
            break
    
    # 对角线元素即为特征值
    return [A[i][i] for i in range(n)]