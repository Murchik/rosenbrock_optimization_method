import math

r = 6


def func_evaluate_1(func, x, d1, lm1):
    if func.__name__ == "func1":
        res = '(((3*((x1)*(x1)))-(x2))**2) + (((2*(x1))-(3*(x2)))**2)'
    elif func.__name__ == "func2":
        res = '(9*((x1)*(x1)))+(16*((x2)*(x2)))-90*(x1)-128*(x2)'
    else:
        res = ''
    zamena1 = 'x[0] + (lm1 * d1[0])'
    zamena2 = 'x[1] + (lm1 * d1[1])'
    res = res.replace('x1', zamena1)
    res = res.replace('x2', zamena2)
    res = res.replace('x[0]', str(x[0]))
    res = res.replace('x[1]', str(x[1]))
    res = res.replace('d1[0]', str(d1[0]))
    res = res.replace('d1[1]', str(d1[1]))
    return round(eval(res), r)


def func_evaluate_2(func, y2, d2, lm2):
    if func.__name__ == "func1":
        res = '(((3*((x1)*(x1)))-(x2))**2) + (((2*(x1))-(3*(x2)))**2)'
    elif func.__name__ == "func2":
        res = '(9*((x1)*(x1)))+(16*((x2)*(x2)))-90*(x1)-128*(x2)'
    else:
        res = ''
    zamena1 = 'y2[0] + (lm2 * d2[0])'
    zamena2 = 'y2[1] + (lm2 * d2[1])'
    res = res.replace('x1', zamena1)
    res = res.replace('x2', zamena2)
    res = res.replace('y2[0]', str(y2[0]))
    res = res.replace('y2[1]', str(y2[1]))
    res = res.replace('d2[0]', str(d2[0]))
    res = res.replace('d2[1]', str(d2[1]))
    return round(eval(res), r)


def golden_search_1(func, x, d1):
    a = -100
    b = 100
    l = 0.001
    alpha = 0.618
    lm1 = round(a + (1 - alpha) * (b - a), r)
    mu1 = round((a + alpha * (b - a)), r)
    # Step 1
    while True:
        if b - a < l:
            result = round((a + b) / 2, r)
            break
        else:
            if func_evaluate_1(func, x, d1, lm1) > func_evaluate_1(func, x, d1, mu1):
                # Step 2
                a = lm1
                b = b
                lm1 = mu1
                mu1 = round(a + alpha * (b - a), r)
            else:
                # Step 3
                a = a
                b = mu1
                mu1 = lm1
                lm1 = round(a + (1 - alpha) * (b - a), r)
    return result


def golden_search_2(func, y2, d2):
    a = -100
    b = 100
    l = 0.001
    alpha = 0.618
    lm2 = round(a + (1 - alpha) * (b - a), r)
    mu2 = round((a + alpha * (b - a)), r)
    # Step 1
    while True:
        if b - a < l:
            ResGoldCartch2 = round((a + b) / 2, r)
            break
        else:
            if func_evaluate_2(func, y2, d2, lm2) > func_evaluate_2(func, y2, d2, mu2):
                # Step 2
                a = lm2
                b = b
                lm2 = mu2
                mu2 = round(a + alpha * (b - a), r)
            else:
                # Step 3
                a = a
                b = mu2
                mu2 = lm2
                lm2 = round(a + (1 - alpha) * (b - a), r)
    return ResGoldCartch2


def get_ortogonals(lm1, lm2, d1, d2):

    a1 = []
    a1.append(round(lm1 * (d1[0]) + lm2 * (d2[0]), r))
    a1.append(round(lm1 * (d1[1]) + lm2 * (d2[1]), r))

    a2 = []
    a2.append(round(lm2 * (d2[0]), r))
    a2.append(round(lm2 * (d2[1]), r))

    b1 = a1

    d1[0] = round((b1[0]) / (math.sqrt(((b1[0]) ** 2) + ((b1[1]) ** 2))), r)
    d1[1] = round((b1[1]) / (math.sqrt(((b1[0]) ** 2) + ((b1[1]) ** 2))), r)

    b2 = []
    b2.append(round((a2[0]) - (a2[0]) * (d1[0]) * (d1[0]), r))
    b2.append(round((a2[1]) - (a2[1]) * (d1[1]) * (d1[1]), r))

    d2[0] = round((b2[0]) / (math.sqrt(((b2[0]) ** 2) + ((b2[1]) ** 2))), r)
    d2[1] = round((b2[1]) / (math.sqrt(((b2[0]) ** 2) + ((b2[1]) ** 2))), r)

    return d1, d2


def new_point_1(lm1, y1, d1):
    y2 = []
    y2.append(round(y1[0] + (lm1 * (d1[0])), r))
    y2.append(round(y1[1] + (lm1 * (d1[1])), r))
    return y2


def new_point_2(lm2, y2, d2):
    y3 = []
    y3.append(round(y2[0] + (lm2 * (d2[0])), r))
    y3.append(round(y2[1] + (lm2 * (d2[1])), r))
    return y3
