def poly_term_derivative(c: float, x: float, n: float) -> float:
    
    x_multiplier = c * n
    other_x = x ** (n - 1)
    output = x_multiplier * other_x
    return output    

pass