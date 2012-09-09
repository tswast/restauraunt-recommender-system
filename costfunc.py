
import numpy as np

N_FEATURES = 10

def cost(x_in, r, y):
    """x_in, is a 1-d array,
    with x parameters for all businesses, and theta for all users.

    r is a boolean matrix, indicating where ratings are present.
    y is a matrix of ratings. (n_businesses x n_users)
    """
    # get parameters
    n_bizs = r.shape[0]
    n_users = r.shape[1]

    # get x and theta matrices from x_in
    x = x_in[:N_FEATURES*n_bizs].reshape((n_bizs, N_FEATURES))
    theta = x_in[N_FEATURES*n_bizs:].reshape((n_users, N_FEATURES))

    j = np.sum(np.asarray(
        np.asmatrix(x) * np.asmatrix(theta.transpose()) - y)[r] ** 2.0)
    return j

def cost_grad(x_in, r, y):
    """x_in, is a 1-d array,
    with x parameters for all businesses, and theta for all users.

    r is a boolean matrix, indicating where ratings are present.
    y is a matrix of ratings. (n_businesses x n_users)
    """
    # get parameters
    n_bizs = r.shape[0]
    n_users = r.shape[1]

    # get x and theta matrices from x_in
    x = x_in[:N_FEATURES*n_bizs].reshape((n_bizs, N_FEATURES))
    theta = x_in[N_FEATURES*n_bizs:].reshape((n_users, N_FEATURES))
    
    predicted_error = np.asarray(
            np.asmatrix(x) * np.asmatrix(theta.transpose()) - y
            ) * r

    j_x = np.asmatrix(predicted_error) * np.asmatrix(theta)
    j_theta = np.asmatrix(predicted_error.transpose()) * np.asmatrix(x)

    return np.asarray(np.hstack([j_x.ravel(), j_theta.ravel()])).ravel()


