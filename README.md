# Filtrage-de-Kalman

This projects shows an implementation of the Kalman filter for linear state equations and the extended Kalman filter for non linear equations (we simulate the case of a radar that measures the angle and distance of the target).   

## Classical Kalamn Filter

### 1. Trajectory simulation 

In the script [utils.py](utils.py), the code simulates a trajectory and generates observations based on a linear state-space. 

The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps using a linear model. 

$$\mathsf{x}_i = \mathsf{F}\mathsf{x}_{i-1} + \mathsf{U}$$

$$\mathbb{N} = \{ a \in \mathbb{Z} : a > 0 \}$$


The function `creer_trajectoire(F, Q, x_init, T)` generates a trajectory of states over 𝑇 time steps using a non-linear model.

### 2. Trajectory simulation 
