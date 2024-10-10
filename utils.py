import numpy as np
import matplotlib.pyplot as plt


def creer_trajectoire(F,Q,x_init,T):
    x_init=np.array([[3],
                     [40],
                     [-4],
                     [20]])
    x_kalm=x_init
    vecteur_x=np.zeros((T,4))
    vecteur_x[0]=x_kalm.T
    for i in range(1,T):
        U=np.random.multivariate_normal(np.array([0,0,0,0]),Q)
        x=vecteur_x[i-1]
        np.reshape(x,(1,4))
        vecteur_x[i]=np.dot(x,F.T)+U.T
    return vecteur_x.T


def creer_observations(H,R,vecteur_x,T):
    vecteur_y=np.zeros((T,2))
    for i in range(1,T):
        V=np.random.multivariate_normal(np.array([0,0]),R)
        vecteur_y[i]=np.dot(vecteur_x.T[i],H.T)+V.T
    return vecteur_y.T


def MSE(x,y):
    return ((x - y)**2).mean()


def RMSE(x,y,T):
    return (MSE(x,y)**(1/2))/T