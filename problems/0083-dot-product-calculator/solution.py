import numpy as np

def calculate_dot_product(vec1, vec2):
    y = 0
    p = 0

    while p < len(vec1):
        y = y + vec1[p] * vec2[p]
        p = p + 1

    return y