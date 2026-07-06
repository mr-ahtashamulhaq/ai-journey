"""
Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])?
"""

import numpy as np

P0 = np.random.uniform(-10,10,(10,2))
P1 = np.random.uniform(-10,10,(10,2))
p  = np.random.uniform(-10,10,( 1,2))

def distance_faster(P0,P1,p):
        #Reference: https://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html

    v = P1- P0 
    v[:,[0,1]] = v[:,[1,0]]
    v[:,1]*=-1 
    norm = np.linalg.norm(v,axis=1)   
    r = P0 - p
    d = np.abs(np.einsum("ij,ij->i",r,v)) / norm 

    return d

print(distance_faster(P0, P1, p))

##--------------- OR ---------------##
def distance_slower(P0, P1, p):
    T = P1 - P0
    L = (T**2).sum(axis=1)
    U = -((P0[:,0]-p[...,0])*T[:,0] + (P0[:,1]-p[...,1])*T[:,1]) / L
    U = U.reshape(len(U),1)
    D = P0 + U*T - p
    return np.sqrt((D**2).sum(axis=1))

print(distance_slower(P0, P1, p))
