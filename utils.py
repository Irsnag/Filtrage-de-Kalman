import numpy as np
import matplotlib.pyplot as plt
import math


def creer_trajectoire(F,Q,x_init,T):
    vecteur_x=np.zeros((T,4))
    vecteur_x[0]=x_init.T
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


def radar(vecteur_x):
    px=vecteur_x[0]
    py=vecteur_x[2]
    return np.array([[math.atan(py/px)],[math.sqrt(px**2+py**2)]])
  
  
def creer_trajectoire_radar(F,Q,x_init,T):
    vecteur_x=np.zeros((T,4))
    vecteur_x[0]=x_init.T
    for i in range(1,T):
        U=np.random.multivariate_normal(np.array([0,0,0,0]),Q)
        x=vecteur_x[i-1]
        np.reshape(x,(1,4))
        vecteur_x[i]=np.dot(x,F.T)+U.T
    return vecteur_x.T


def creer_observations_radar(R,vecteur_x,T):
    vecteur_y=np.zeros((2,T))
    for i in range(1,T):
        px=vecteur_x[0,i]
        py=vecteur_x[2,i]
        V=np.random.multivariate_normal(np.array([0,0]),R)
        vecteur_y[(0,i)]=math.atan(py/px)+V[0]
        vecteur_y[(1,i)]=math.sqrt(px**2+py**2)+V[1]
    return vecteur_y



def MSE(x,y):
    return ((x - y)**2).mean()


def RMSE(x,y,T):
    return (MSE(x,y)**(1/2))/T