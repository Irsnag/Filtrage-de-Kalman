import math
import numpy as np
import matplotlib.pyplot as plt
from utils import *

def Jacobien(a, b):
    # Jacobian matrix computation for radar system
    Jg = np.array([[-b / (a**2 + b**2), 0, a / (a**2 + b**2), 0],
                   [a / np.sqrt(a**2 + b**2), 0, b / np.sqrt(a**2 + b**2), 0]], dtype='float')
    return Jg

def filtre_de_kalman(F, Q, R, y_k, x_kalm_prec, P_kalm_prec):
    # Prediction step
    P = Q + F @ P_kalm_prec @ F.T  # Predicted covariance
    x = F @ x_kalm_prec  # Predicted state

    # Update step
    J_k = Jacobien(x[0], x[2])  # Jacobian matrix at predicted state
    H = J_k  # Observation model (Jacobian)
    
    # Kalman gain
    K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
    
    # Updated state and covariance estimate
    x_kalm_k = np.reshape(x, (4, 1)) + K @ (y_k - np.reshape(H @ x, (2, 1)))
    P_kalm_k = (np.eye(np.shape(P)[0]) - K @ H) @ P
    
    return x_kalm_k, P_kalm_k

# Initialize parameters
pi = math.pi
sigma_angle = pi / 180  # Angle noise (radians)
sigma_dist = 1  # Distance noise
Te = 1  # Time step
T = 100  # Total number of steps
sigma_Q = 10  # Process noise variance

# System dynamics matrix
F = np.array([[1, Te, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, Te],
              [0, 0, 0, 1]])

# Process noise covariance matrix
Q = sigma_Q**2 * np.array([[Te**3 / 3, Te**2 / 2, 0, 0],
                           [Te**2 / 2, Te, 0, 0],
                           [0, 0, Te**3 / 3, Te**2 / 2],
                           [0, 0, Te**2 / 2, Te]])

# Measurement noise covariance matrix
R = np.array([[sigma_angle**2, 0],
              [0, sigma_dist**2]])

# Initial state [x_position, x_velocity, y_position, y_velocity]
x_init = np.array([[3],
                   [40],
                   [-4],
                   [20]])

# Generate true trajectory and noisy observations
X = creer_trajectoire_radar(F, Q, x_init, T)  # True trajectory
Y = creer_observations_radar(R, X, T)  # Noisy radar observations

# Initialize Kalman filter variables
x_est = np.zeros((4, T))  # Estimated states
x_est[:, 0] = x_init[:, 0]  # Initial state
P = np.eye(4)  # Initial covariance matrix
P_kalm_prec = P  # Previous covariance

# Kalman filtering loop
for k in range(1, T):
    x_kalm_prec = x_est[:, k - 1]  # Previous state estimate
    y_k = Y[:, k]  # Current observation

    # Predicted state and Jacobian-based innovation
    x = F @ x_kalm_prec
    r_k = radar(x) - np.reshape(Jacobien(x[0], x[2]) @ x, (2, 1))
    
    # Reshape observation and apply Kalman filter
    y_k = np.reshape(y_k, (2, 1))
    x_int, P_kalm_prec = filtre_de_kalman(F, Q, R, y_k - r_k, x_kalm_prec, P_kalm_prec)
    
    # Update state estimates
    for l in range(4):
        x_est[l, k] = x_int[l]

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot true trajectory (blue line)
plt.plot(X[0, :], X[2, :], label='True Trajectory', color='blue')

# Plot Kalman filter estimates (green line)
plt.plot(x_est[0, :], x_est[2, :], label=' Extended Kalman Filter Estimate', color='green')

# Add title, labels, and legend
plt.title('Kalman Filter: Radar-Based Tracking')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Add grid for better readability
plt.grid(True)

# Show the plot
plt.show()
