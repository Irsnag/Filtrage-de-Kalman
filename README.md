# Filtrage-de-Kalman

This projects shows an implementation of the Kalman filter for linear state equations and the extended Kalman filter for non linear equations (we simulate the case of a radar that measures the angle and distance of the target).   

## Classical Kalamn Filter

### 1. Trajectory simulation 

In the script [utils.py](utils.py), the code simulates a trajectory and generates observations based on a linear state-space. 

The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps. 

The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps in the case of a radar.

The transition equation is given by :

$$\mathbb{x_i} = \mathbb{F}\mathsf{x_{i-1}} + \mathbb{U_i}$$

Each hidden state $$\mathbb{x_i}$$ gives the position and speed along the $$\mathbb{x}$$ and $$\mathbb{y}$$ axes. 

### 2. Observation space

The function `creer_observations(H,R,vecteur_x,T)` generates an observation based on a linear measurement model with Gaussian noise :

$$\mathbb{y_i} = \mathbb{H}\mathsf{x_{i-1}} + \mathbb{V_i}$$

The function `creer_observations_radar(H,R,vecteur_x,T)` generates an observation based on a linear measurement model with Gaussian noise :

$$\mathbb{y_i} = \mathbb{f}(\mathsf{x_{i-1}}) + \mathbb{V_i}$$
