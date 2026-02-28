import numpy as np

class SA:
    def __init__(s, d, a=0.6, b=0.3):
        s.d=d
        s.th=np.zeros(d)
        s.w=np.zeros(d)
        s.a=a
        s.b=b
        
    def an(s, n):
        return (n+1)**-s.a
        
    def bn(s, n): return (n+1)**-s.b