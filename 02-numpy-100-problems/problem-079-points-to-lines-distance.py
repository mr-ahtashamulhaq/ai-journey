"""
Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])?
"""

import numpy as np

# based on distance function from previous question
P0 = np.random.uniform(-10, 10, (10,2))
P1 = np.random.uniform(-10,10,(10,2))
p = np.random.uniform(-10, 10, (10,2))
print(np.array([distance(P0,P1,p_i) for p_i in p]))

def distance_points_to_lines(p: np.ndarray, p_1: np.ndarray, p_2: np.ndarray) -> np.ndarray:
    x_0, y_0 = p.T  # Shape -> (n points, )
    x_1, y_1 = p_1.T  # Shape -> (n lines, )
    x_2, y_2 = p_2.T  # Shape -> (n lines, )

    # Displacement vector coordinates from p_1 -> p_2
    dx = x_2 - x_1  # Shape -> (n lines, )
    dy = y_2 - y_1  # Shape -> (n lines, )

    # The 'cross product' term
    cross_term = x_2 * y_1 - y_2 * x_1  # Shape -> (n lines, )

    # Broadcast x_0, y_0 (n points, 1) and dx, dy, cross_term (1, n lines) -> (n points, n lines)
    numerator = np.abs(
        dy[np.newaxis, :] * x_0[:, np.newaxis]
        - dx[np.newaxis, :] * y_0[:, np.newaxis]
        + cross_term[np.newaxis, :]
    )
    denominator = np.sqrt(dx**2 + dy**2)  # Shape -> (n lines, )

    # Shape (n points, n lines) / (1, n_lines) -> (n points, n lines)
    return numerator / denominator[np.newaxis, :]

distance_points_to_lines(p, P0, P1)
