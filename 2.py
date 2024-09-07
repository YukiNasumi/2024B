cases = [
    {'p1': 0.10, 'C_d1': 2, 'p2': 0.10, 'C_d2': 3, 'p_c': 0.10, 'C_a': 6, 'C_dc': 3, 'C_s': 56, 'C_r': 6, 'C_t': 5},
    {'p1': 0.20, 'C_d1': 2, 'p2': 0.20, 'C_d2': 3, 'p_c': 0.20, 'C_a': 6, 'C_dc': 3, 'C_s': 56, 'C_r': 6, 'C_t': 5},
    {'p1': 0.10, 'C_d1': 2, 'p2': 0.10, 'C_d2': 3, 'p_c': 0.10, 'C_a': 6, 'C_dc': 3, 'C_s': 56, 'C_r': 30, 'C_t': 5},
    {'p1': 0.20, 'C_d1': 1, 'p2': 0.20, 'C_d2': 1, 'p_c': 0.20, 'C_a': 6, 'C_dc': 2, 'C_s': 56, 'C_r': 30, 'C_t': 5},
    {'p1': 0.10, 'C_d1': 8, 'p2': 0.20, 'C_d2': 1, 'p_c': 0.10, 'C_a': 6, 'C_dc': 2, 'C_s': 56, 'C_r': 10, 'C_t': 5},
    {'p1': 0.05, 'C_d1': 2, 'p2': 0.05, 'C_d2': 3, 'p_c': 0.05, 'C_a': 6, 'C_dc': 3, 'C_s': 56, 'C_r': 10, 'C_t': 40},
]
def dynamic_programming(case, weight_cost=0.5, weight_defect=0.5):
    # 提取参数
    p1, C_d1, p2, C_d2, p_c, C_a, C_dc, C_s, C_r, C_t = (
        case['p1'], case['C_d1'], case['p2'], case['C_d2'],
        case['p_c'], case['C_a'], case['C_dc'], case['C_s'],
        case['C_r'], case['C_t']
    )
    
    # 定义状态空间
    V = {}

    # 定义状态转移方程
    def compute_cost(s1, s2, s3, s4, iteration=0):
        if iteration > 10:  # 防止无限循环，设置最大迭代次数
            return float('inf')
        
        if (s1, s2, s3, s4) in V:
            return V[(s1, s2, s3, s4)]
        
        # 成本计算
        cost = s1 * C_d1 + s2 * C_d2 + s3 * C_dc
        
        # 成品次品率计算
        p_final = 1 - (1 - p1 * (1 - s1)) * (1 - p2 * (1 - s2)) * (1 - p_c * s3)
        
        # 市场销售或调换损失
        if s3:
            # 成品检测后，次品直接拆解或报废
            cost += p_final * (compute_cost(s1, s2, s3, s4=1, iteration=iteration+1) if s4 else 0)
        else:
            # 成品未检测，可能引发调换损失
            cost += p_final * C_r
        
        # 装配成本
        cost += C_a
        
        # 计算综合目标函数（结合成本和次品率）
        combined_cost = weight_cost * cost + weight_defect * p_final * 100  # 次品率影响可以放大一些
        
        V[(s1, s2, s3, s4)] = combined_cost
        return combined_cost

    # 遍历所有状态组合，寻找最优的决策
    min_combined_cost = float('inf')
    best_decision = None
    
    for s1 in [0, 1]:
        for s2 in [0, 1]:
            for s3 in [0, 1]:
                for s4 in [0, 1]:
                    current_combined_cost = compute_cost(s1, s2, s3, s4)
                    if current_combined_cost < min_combined_cost:
                        min_combined_cost = current_combined_cost
                        best_decision = (s1, s2, s3, s4)
    
    return min_combined_cost, best_decision, V

# 计算每个情况的最优决策
for i, case in enumerate(cases):
    min_cost, best_decision, value_table = dynamic_programming(case)
    print(f"情况 {i + 1}: 最小综合成本 = {min_cost}, 最优决策 (s1, s2, s3, s4) = {best_decision}")
