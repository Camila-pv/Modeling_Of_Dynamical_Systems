def simulate_equation(x_cte, r_x, K, num_steps):
    results = [x_cte]
    
    for _ in range(num_steps):
        x_cte = x_cte + r_x * x_cte *(1 - x_cte / K)
        results.append(x_cte)
        
    return results

# Init conds
x_cte_initial = [0, 0.2]
rx = 2.0
K_cap = 10.0