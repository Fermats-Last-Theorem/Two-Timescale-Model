import numpy as np

class MDP:
    def __init__(s):
        s.d = 5
        s.g = 0.9
        s.st = 2 
        
    def smp(s):
        o = s.st
        s.st += np.random.choice([-1, 1])
        r = 0
        dn = False
        
        if s.st <= 0:
            s.st = 0
            r = -1
            dn = True
        elif s.st >= 4:
            s.st = 4
            r = 1
            dn = True
            
        u = np.zeros(s.d)
        u[o] = 1
        v = np.zeros(s.d)
        v[s.st] = 1
        
        if dn:
            s.st = 2
            v = np.zeros(s.d) 
            
        return u, v, r