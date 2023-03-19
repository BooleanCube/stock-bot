import numpy as np

def linear_regression(pts):
    x = np.array([pt[0] for pt in pts])
    y = np.array([pt[1] for pt in pts])
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    return B1, B0


def corr_coef(pts):
    x = np.array([pt[0] for pt in pts]).reshape(-1, 1)
    y = np.array([pt[1] for pt in pts])
    N = len(x)

    num = (N * (x * y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x ** 2).sum() - x.sum() ** 2) * (N * (y ** 2).sum() - y.sum() ** 2))
    R = num / den
    return R
