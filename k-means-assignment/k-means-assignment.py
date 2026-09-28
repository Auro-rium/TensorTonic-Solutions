import numpy as np


def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    points = np.array(points)
    centroids = np.array(centroids)

    diff = points[:, np.newaxis, :] - centroids[np.newaxis, :, :]

    distances = np.sum(diff ** 2, axis=2)

    return np.argmin(distances, axis=1).tolist()