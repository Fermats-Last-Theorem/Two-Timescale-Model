import matplotlib.pyplot as plt
import numpy as np

def plt_err(r, th_star, ws=50):
    x=[k['n'] for k in r]
    
    
    err=[np.linalg.norm(k['t'] - th_star) for k in r]
    w=[np.linalg.norm(k['w']) for k in r]
    
    err_s=np.convolve(err, np.ones(ws)/ws, 'valid')
    ws_=np.convolve(w, np.ones(ws)/ws, 'valid')
    xs=x[:len(err_s)]
    
    plt.plot(xs, err_s, label='||th - th*||')
    plt.plot(xs, ws_, label='||w||')
    plt.yscale('log')
    plt.legend()
    plt.show()