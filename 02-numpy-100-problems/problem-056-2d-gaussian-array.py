"""
Generate a generic 2D Gaussian-like array
"""

import numpy as np

X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
sigma, mu = 1.0, 0.0
G = np.exp(-((X - mu) ** 2 + (Y - mu) ** 2) / (2.0 * sigma**2))
print(G)

# Another solution using the fact that a 2D Gaussian is separable
x = np.linspace(-1, 1, 10)
y = np.linspace(-1, 1, 10)
gx = np.exp(-((x - mu) ** 2 / (2.0 * sigma**2)))
gy = np.exp(-((y - mu) ** 2 / (2.0 * sigma**2)))
G = gy[:, None] * gx[None, :]
print(G)
