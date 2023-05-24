import numpy as np
import optimize as op


def func1(x):
    """F1(x) = (3X1^2 - X2)^2 + (2X1 - 3X2)^2"""
    return (3 * x[0] ** 2 - x[1]) ** 2 + (2 * x[0] - 3 * x[1]) ** 2


def func2(x):
    """F2(x) = 9X1^2 + 16X2^2 - 90X1 - 128X2"""
    return 9 * x[0] ** 2 + 16 * x[1] ** 2 - 90 * x[0] - 128 * x[1]


def main():
    op.optimize(func=func1, x0=np.array([0.0, 1.0]), eps=0.1)
    op.optimize(func=func1, x0=np.array([0.0, 1.0]), eps=0.01)
    op.optimize(func=func1, x0=np.array([0.0, 1.0]), eps=0.001)

    op.optimize(func=func2, x0=np.array([0.0, 0.0]), eps=0.1)
    op.optimize(func=func2, x0=np.array([0.0, 0.0]), eps=0.01)
    op.optimize(func=func2, x0=np.array([0.0, 0.0]), eps=0.001)


if __name__ == "__main__":
    main()
