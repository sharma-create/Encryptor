import numpy as np
import matplotlib.pyplot as plt

# Sample input
x = np.linspace(-5, 5, 100)

# Activation functions
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Compute outputs
relu_out = relu(x)
sigmoid_out = sigmoid(x)
tanh_out = tanh(x)

print("ReLU Range: [0, ∞)")
print("Sigmoid Range: (0,1)")
print("Tanh Range: (-1,1)")

# Plot
plt.plot(x, relu_out, label="ReLU")
plt.plot(x, sigmoid_out, label="Sigmoid")
plt.plot(x, tanh_out, label="Tanh")
plt.legend()
plt.title("Activation Functions")
plt.show()