import numpy as np


##########
# PRIMES #
##########


def compute_greatest_common_divider(p, q):
    """Compute the greatest common divider of two integers p and q.

    Parameters
    ----------
    p : int
        First integer.
    q : int
        Second integer.

    Returns
    -------
    int
        The greatest common divider of p and q.
    """
    while q != 0:
        p, q = q, p % q
    return p


def compute_coprime_factors(Nc, length, start=1, update=1):
    """Compute a list of coprime factors of Nc.

    Parameters
    ----------
    Nc : int
        Number to factorize.
    length : int
        Number of coprime factors to compute.
    start : int, optional
        First number to check. The default is 1.
    update : int, optional
        Increment between two numbers to check. The default is 1.

    Returns
    -------
    list
        List of coprime factors of Nc.
    """
    count = start
    coprimes = []
    while len(coprimes) < length:
        if compute_greatest_common_divider(Nc, count) == 1:
            coprimes.append(count)
        count += update
    return coprimes


#############
# ROTATIONS #
#############


def R2D(theta):
    """Initialize 2D rotation matrix.

    Parameters
    ----------
    theta : float
        Rotation angle in rad.

    Returns
    -------
    np.ndarray
        2D rotation matrix.
    """
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


def Rx(theta):
    """Initialize 3D rotation matrix around x axis.

    Parameters
    ----------
    theta : float
        Rotation angle in rad.

    Returns
    -------
    np.ndarray
        2D rotation matrix.
    """
    return np.array(
        [
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)],
        ]
    )


def Ry(theta):
    """Initialize 3D rotation matrix around y axis.

    Parameters
    ----------
    theta : float
        Rotation angle in rad.

    Returns
    -------
    np.ndarray
        2D rotation matrix.
    """
    return np.array(
        [
            [np.cos(theta), 0, np.sin(theta)],
            [0, 1, 0],
            [-np.sin(theta), 0, np.cos(theta)],
        ]
    )


def Rz(theta):
    """Initialize 3D rotation matrix around z axis.

    Parameters
    ----------
    theta : float
        Rotation angle in rad.

    Returns
    -------
    np.ndarray
        2D rotation matrix.
    """
    return np.array(
        [
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1],
        ]
    )


def Rv(v1, v2, normalize=True):
    """Initialize 3D rotation matrix from two vectors.

    Initialize a 3D rotation matrix from two vectors using Rodrigues's rotation
    formula. Note that the rotation is carried around the axis orthogonal to both
    vectors from the origin, and therefore is undetermined when both vectors
    are co-linear.

    Parameters
    ----------
    v1 : np.ndarray
        Source vector.
    v2 : np.ndarray
        Target vector.
    normalize : bool, optional
        Normalize the vectors. The default is True.

    Returns
    -------
    np.ndarray
        3D rotation matrix.
    """
    if normalize:
        v1, v2 = v1 / np.linalg.norm(v1), v2 / np.linalg.norm(v2)
    cos_theta = np.dot(v1, v2)
    v3 = np.cross(v1, v2)
    cross_matrix = np.cross(v3, np.identity(v3.shape[0]) * -1)
    return np.identity(3) + cross_matrix + cross_matrix @ cross_matrix / (1 + cos_theta)


def Ra(vector, theta):
    """Initialize 3D rotation matrix around an arbitrary vector.

    Initialize a 3D rotation matrix to rotate around `vector` by an angle `theta`.
    It corresponds to the generalized formula with `Rx`, `Ry` and `Rz` as subcases.

    Parameters
    ----------
    vector : np.ndarray
        Vector defining the rotation axis, automatically normalized.
    theta : float
        Angle in radians defining the rotation around `vector`.

    Returns
    -------
    np.ndarray
        3D rotation matrix.
    """
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    v_x, v_y, v_z = vector / np.linalg.norm(vector)
    return np.array(
        [
            [
                cos_t + v_x ** 2 * (1 - cos_t),
                v_x * v_y * (1 - cos_t) + v_z * sin_t,
                v_x * v_z * (1 - cos_t) - v_y * sin_t,
            ],
            [
                v_y * v_x * (1 - cos_t) - v_z * sin_t,
                cos_t + v_y ** 2 * (1 - cos_t),
                v_y * v_z * (1 - cos_t) + v_x * sin_t,
            ],
            [
                v_z * v_x * (1 - cos_t) + v_y * sin_t,
                v_z * v_y * (1 - cos_t) - v_x * sin_t,
                cos_t + v_z ** 2 * (1 - cos_t),
            ],
        ]
    )


#############
# FIBONACCI #
#############


def generate_fibonacci_lattice(nb_points, epsilon=0.25):
    angle = (1 + np.sqrt(5)) / 2
    fibonacci_square = np.zeros((nb_points, 2))
    fibonacci_square[:, 0] = (np.arange(nb_points) / angle) % 1
    fibonacci_square[:, 1] = (np.arange(nb_points) + epsilon) / (
        nb_points - 1 + 2 * epsilon
    )
    return fibonacci_square


def generate_fibonacci_circle(nb_points, epsilon=0.25):
    fibonacci_square = generate_fibonacci_lattice(nb_points, epsilon)
    radius = np.sqrt(fibonacci_square[:, 1])
    angles = 2 * np.pi * fibonacci_square[:, 0]

    fibonacci_circle = np.zeros((nb_points, 2))
    fibonacci_circle[:, 0] = radius * np.cos(angles)
    fibonacci_circle[:, 1] = radius * np.sin(angles)
    return fibonacci_circle


def generate_fibonacci_sphere(nb_points, epsilon=0.25):
    fibonacci_square = generate_fibonacci_lattice(nb_points, epsilon)
    theta = 2 * np.pi * fibonacci_square[:, 0]
    phi = np.arccos(1 - 2 * fibonacci_square[:, 1])

    fibonacci_sphere = np.zeros((nb_points, 3))
    fibonacci_sphere[:, 0] = np.cos(theta) * np.sin(phi)
    fibonacci_sphere[:, 1] = np.sin(theta) * np.sin(phi)
    fibonacci_sphere[:, 2] = np.cos(phi)
    return fibonacci_sphere
