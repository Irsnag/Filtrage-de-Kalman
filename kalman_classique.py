import numpy as np
import matplotlib.pyplot as plt
from utils import *

def filtre_de_kalman(F, Q, H, R, y_k, x_kalm_prec, P_kalm_prec):
    # Prediction step
    P = Q + F @ P_kalm_prec @ F.T  # Predicted covariance
    x = F @ x_kalm_prec  # Predicted state
    
    # Update step
    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)  # Kalman gain
    x_kalm_k = x + K @ (y_k - H @ x)  # Updated state estimate
    P_kalm_k = (np.eye(np.shape(P)[0]) - K @ H) @ P  # Updated covariance estimate
    
    return x_kalm_k, P_kalm_k

# Time step, number of steps, and noise parameters
Te = 1
T = 100
sigma_Q = 1
sigma_px = 30
sigma_py = 30
c = 1

# Define initial position
x_init=np.array([[3],
                 [40],
                 [-4],
                 [20]])
x_kalm=x_init

# Define system matrices
F = np.array([[1, Te, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, Te],
              [0, 0, 0, 1]])

H = np.array([[1, 0, 0, 0],
              [0, 0, 1, 0]])

Q = sigma_Q**2 * np.array([[Te**3/3, Te**2/2, 0, 0],
                           [Te**2/2, Te, 0, 0],
                           [0, 0, Te**3/3, Te**2/2],
                           [0, 0, Te**2/2, Te]])

R = np.array([[sigma_px**2, 0],
              [0, sigma_py**2]])

I = np.eye(4)

# Generate trajectory and observations
X = creer_trajectoire(F, Q, x_init, T)  # True trajectory
Y = creer_observations(H, R, X, T)  # Noisy observations

# Plot the true trajectory and noisy observations
plt.figure(figsize=(10, 6))
plt.plot(X[0, :], X[2, :], label="True Trajectory", color='blue')  # True trajectory
plt.scatter(Y[0, :], Y[1, :], c='red', label="Noisy Observations", alpha=0.6)  # Noisy observations

# Initialize Kalman filter
x_est = np.zeros((4, T))  # Estimated states
x_est[:, 0] = x_init[:, 0]  # Initial state
P = np.eye(4)  # Initial covariance matrix
P_kalm_prec = P  # Previous covariance

# Kalman filtering loop
for k in range(1, T):
    x_kalm_prec = x_est[:, k - 1]  # Previous state estimate
    y_k = Y[:, k]  # Current observation
    # Apply Kalman filter
    x_est[:, k], P_kalm_prec = filtre_de_kalman(F, Q, H, R, y_k, x_kalm_prec, P_kalm_prec)

# Plot the Kalman filter estimates
plt.plot(x_est[0, :], x_est[2, :], c='green', label="Kalman Filter Estimate")  # Estimated trajectory

# Add title, labels, and legend
plt.title('Kalman Filter: True Trajectory, Noisy Observations, and Estimates')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
