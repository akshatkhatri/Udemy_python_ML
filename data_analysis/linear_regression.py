import random
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
np.random.seed(42)

# Generate random data
x_values = np.random.rand(100,1) * 2

# Equation for y = 4+3x + Noise
y_values = 4 + 3*(x_values) + np.random.randn(100,1)

# Function to calculate Mean Squared Error
def mean_squared_error(slope, intercept, x_values, y_values):
    MSE = 0  # Mean Squared Error
    n = len(x_values)

    for xi, yi in zip(x_values, y_values):
        y_pred = (slope * xi) + (intercept)
        y_actual = yi
        error = y_pred - y_actual
        MSE += error ** 2
    return MSE / n

# Gradient Descent Function
def gradient_descent(learning_rate, x_values, y_values, slope, intercept):
    n = len(x_values)

    for i in range(1000):
        gradient_wrt_intercept = 0
        gradient_wrt_slope = 0

        if i % 50 == 0:
            print(f'Mean squared Error is -> {mean_squared_error(slope, intercept, x_values, y_values)}')
            sleep(2)

        for xi, yi in zip(x_values, y_values):
            gradient_wrt_intercept += (slope * xi + intercept - yi)
            gradient_wrt_slope += ((slope * xi + intercept - yi) * xi)
        gradient_wrt_intercept += (2 / n) * gradient_wrt_intercept
        gradient_wrt_slope += (2 / n) * gradient_wrt_slope
        intercept_step_size = gradient_wrt_intercept * learning_rate
        slope_step_size = gradient_wrt_slope * learning_rate

        intercept -= intercept_step_size
        slope -= slope_step_size

    return slope, intercept

# Picking up values for the parameters
slope = 0
intercept = 0
learning_rate = 0.001
epochs = 1000

predicted_slope, predicted_intercept = gradient_descent(learning_rate, x_values, y_values, slope, intercept)

# Plotting the data and fitted line
plt.scatter(x_values, y_values, color='Green', label='Data Points')
predicted_points = [(predicted_slope * xi + predicted_intercept) for xi in x_values]
plt.plot(x_values, predicted_points, color='Red', label='Fitted Line')

plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()
