import numpy as np

def proj(x, R=10):
    nm = np.linalg.norm(x)
    if nm > R:
        x = x * (R / nm)
    return x