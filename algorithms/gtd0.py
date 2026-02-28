import numpy as np
from .base import SA
from .projection import proj

class GTD(SA):
    def __init__(s, d):
        super().__init__(d)
        s.A = np.eye(d)
        s.b = np.zeros(d)
        
    def upd(s, u, v, r, n, gamma):
            a=s.an(n)
            b=s.bn(n)
            
            dl = r + gamma * np.dot(s.th, v) - np.dot(s.th, u)
            s.w += b * (dl * u - s.w)
            
            s.th += a * (u - gamma * v) * np.dot(u, s.w)
            
            s.th = proj(s.th,n)
            s.w = proj(s.w,n)