import numpy as np
from algorithms.gtd0 import GTD
from envs.simple_mdp import MDP
from utils.logger import Log
from utils.plots import plt_err

def get_th_star(d, g):
    P=np.array([[0,0.5,0],[0.5,0,0.5],[0,0.5,0]])
    R=np.array([-0.5,0,0.5])
    
    I=np.eye(3)
    V=np.linalg.inv(I-g*P).dot(R)
    
    th_star=np.zeros(d)
    th_star[1:4]=V
    return th_star

def run():
    m=MDP()
    g=GTD(m.d)
    l=Log()
    
    th_star = get_th_star(m.d, m.g)
    
    for i in range(1, 50001):
        u,v,r=m.smp()
        g.upd(u,v,r,i,m.g)
        
        if i%100==0:
            l.lg(i,g.th,g.w)
            
    plt_err(l.r, th_star)

if __name__=="__main__":
    run()