from typing import Callable
import dataclasses

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm
from prettytable import PrettyTable

import rosenbrock as rb


@dataclasses.dataclass
class MyOptimizeResult:
    x: np.ndarray
    fx: np.ndarray
    k: int
    path: np.ndarray
    table: str = ""


def optimize(func: Callable, x0: np.ndarray, eps: float) -> None:
    res: MyOptimizeResult = minimize(func, x0, eps)
    print(f"Func: {func.__doc__}\nStart point: {x0}\nEpsilon: {eps}\n{res.table}\nFinal x:{res.x}\nF(x)={res.fx:.4f}\nIterations: {res.k}")
    visualise_func_3d(func, x0, res)


def minimize(func: Callable, x0: np.ndarray, eps: float) -> MyOptimizeResult:
    path = []
    table = PrettyTable()
    table.field_names = ["k", "xk", "F(xk)",
                         "j", "yk", "F(yk)",
                         "dj", "lmj",
                         "yj + delj*dj", "F(yj + delj*dj)"]
    table.float_format = ".3"

    k = 1

    x = x0
    fx = func(x)

    y1 = x
    fy1 = func(y1)
    d1 = [1, 0]
    lm1 = rb.golden_search_1(func, x, d1)

    y2 = rb.new_point_1(lm1, x, d1)
    fy2 = func(y2)
    d2 = [0, 1]
    lm2 = rb.golden_search_2(func, y2, d2)

    y3 = rb.new_point_2(lm2, y2, d2)
    fy3 = func(y3)

    while True:
        path.append([x[0], x[1]])
        table.add_row(
            [x for x in [k, x, fx, 1, y1, fy1, d1, lm1, y2, fy2]])
        table.add_row(
            [x for x in [" ", " ", " ", 2, y2, fy2, d2, lm2, y3, fy3]])

        res = np.sqrt((y3[0] - x[0])**2 + ((y3[1] - x[1])**2))
        if res < eps:
            break

        d1, d2 = rb.get_ortogonals(lm1, lm2, d1, d2)

        k = k + 1

        x = y3
        fx = func(x)

        y1 = x
        fy1 = func(y1)
        lm1 = rb.golden_search_1(func, y1, d1)

        y2 = rb.new_point_1(lm1, y1, d1)
        fy2 = func(y2)
        lm2 = rb.golden_search_2(func, y2, d2)

        y3 = rb.new_point_2(lm2, y2, d2)
        fy3 = func(y3)

    result = MyOptimizeResult(
        x=np.array([y3[0], y3[1]]),
        fx=np.array(res),
        k=k,
        path=np.array(path).T,
        table=str(table))
    return result


def visualise_func_3d(
    func: Callable,  # Func to optimize
    x0: np.ndarray,  # Initial guess
    result: MyOptimizeResult,  # Final result
) -> None:
    # Midpoint between initial guess and result
    midpoint = [(x0[0] + result.x[0]) / 2, (x0[1] + result.x[1]) / 2]
    # Distance between initial guess and result
    distance = np.sqrt((x0[0] - result.x[0]) ** 2 + (x0[1] - result.x[1]) ** 2)
    # How much to plot around mid point
    raduis = distance / 1.3

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.set_xlim(midpoint[0] - raduis, midpoint[0] + raduis)
    ax.set_ylim(midpoint[1] - raduis, midpoint[1] + raduis)

    ax.set_xlabel("X1")
    ax.set_ylabel("X2")

    # Set up contours
    # https://matplotlib.org/stable/gallery/images_contours_and_fields/contours_in_optimization_demo.html#sphx-glr-gallery-images-contours-and-fields-contours-in-optimization-demo-py
    xvec = np.linspace(midpoint[0] - raduis, midpoint[0] + raduis, 100)
    yvec = np.linspace(midpoint[1] - raduis, midpoint[1] + raduis, 100)
    x1, x2 = np.meshgrid(xvec, yvec)
    obj = func([x1, x2])
    # TODO: REFACTOR HARDCODED STEPS
    if func.__name__ == "func1":
        steps = [0.001, 0.1, 1, 2, 4, 8, 16, 32, 64, 128]
    elif func.__name__ == "func2":
        steps = [-470, -400, -256, -128, -64, 0, 64, 128, 256, 512]
    else:
        steps = []
    cntr = ax.contour(x1, x2, obj, steps,
                      colors='black')
    ax.clabel(cntr, fmt="%3.2f", use_clabeltext=True)

    # Set up coloring of contours
    # https://matplotlib.org/stable/gallery/images_contours_and_fields/contourf_log.html
    cs = ax.contourf(x1, x2, obj, locator=ticker.LogLocator(), cmap=cm.PuBu_r)
    cbar = fig.colorbar(cs)

    # Set up arrows for path of optimization
    # http://louistiao.me/notes/visualizing-and-animating-optimization-algorithms-with-matplotlib/
    path = result.path
    ax.quiver(path[0, :-1],
              path[1, :-1],
              path[0, 1:]-path[0, :-1],
              path[1, 1:]-path[1, :-1],
              scale_units='xy',
              angles='xy',
              scale=1,
              color='k')

    # Plot result point
    plt.plot(result.x[0], result.x[1], marker="*", markersize=10, color="red")

    plt.show()
