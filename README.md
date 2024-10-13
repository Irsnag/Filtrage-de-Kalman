# Filtrage-de-Kalman

This projects shows an implementation of the Kalman filter for linear state equations and the extended Kalman filter for non linear equations (we simulate the case of a radar that measures the angle and distance of the target).   

## Classical Kalamn Filter

### 1. Trajectory simulation 

In the script [utils.py](utils.py), the code simulates a trajectory and generates observations based on a linear state-space. 

The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps. 

The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps in the case of a radar.

The transition equation is given by :

$$\mathbb{x_i} = \mathbb{F}\mathsf{x_{i-1}} + \mathbb{U_i}$$

Each hidden state $$\mathbb{x_i}$$ gives the position and velocity along the $$\mathbb{x}$$ and $$\mathbb{y}$$ axes. 

### 2. Observation space

The function `creer_observations(H,R,vecteur_x,T)` generates an observation based on a linear measurement model with Gaussian noise :

$$\mathbb{y_i} = \mathbb{H}\mathsf{x_{i-1}} + \mathbb{V_i}$$

The matrix $$\mathbb{H}$$ hides the velocity of the target and keeps the position in the observation

The function `creer_observations_radar(H,R,vecteur_x,T)` generates an observation based on a non-linear measurement model with Gaussian noise :

$$\mathbb{y_i} = \mathbb{f}(\mathsf{x_{i-1}}) + \mathbb{V_i}$$

The non-linear measurements are based on angle and distance.

### 3. Results

The linear kalman filter can be found in [kalman_classique.py](kalman_classique.py) and the extended version in [kalman_extended.py](kalman_extended.py). You may modify the different parameters to see the results. 

![In the linear case :]([http://url/to/img.png](https://github.com/Irsnag/Filtrage-de-Kalman/blob/main/results/linear.png))

![In the non-linear case :]([http://url/to/img.png](https://github.com/Irsnag/Filtrage-de-Kalman/blob/main/results/non-linear.png))






