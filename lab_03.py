import math


def get_finite_difference_table(xk_array):
    n = len(xk_array)
    table_finite_difference = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        table_finite_difference[i][0] = f(xk_array[i])

    for j in range(1, n):
        for i in range(n - j):
            table_finite_difference[i][j] = (table_finite_difference[i][j - 1] - table_finite_difference[i - 1][j - 1])

    return table_finite_difference


def start_table_interpolation_formula_newton(x_interpolation, xk_array):
    n = len(xk_array)
    h = xk_array[1] - xk_array[0]
    t = (x_interpolation - xk_array[0]) / h
    table_finite_diff = get_finite_difference_table(xk_array)

    polynom = table_finite_diff[0][0]
    for i in range(1, n):
        component = table_finite_diff[0][i] / math.factorial(i)
        for j in range(i):
            component *= (t - j)
        polynom += component

    return polynom


def end_table_interpolation_formula_newton(x_interpolation, xk_array):
    n = len(xk_array)
    h = xk_array[1] - xk_array[0]
    q = (x_interpolation - xk_array[n - 1]) / h
    table_finite_diff = get_finite_difference_table(xk_array)

    polynom = table_finite_diff[n - 1][0]
    for i in range(1, n):
        component = table_finite_diff[n - 1 - i][i] / math.factorial(i)
        for j in range(i):
            component *= (q + j)
        polynom += component

    return polynom


def central_table_first_interpolation_formula_gauss(x_interpolation, xk_array):
    n = len(xk_array)
    h = xk_array[1] - xk_array[0]
    t = (x_interpolation - xk_array[0]) / h
    table_finite_diff = get_finite_difference_table(xk_array)

    m = n // 2
    if n % 2 == 0:
        m -= 1
    polynom = table_finite_diff[m][0]  # для y0 (который в формуле Гаусса - центральный элемент таблицы)
    for i in range(1, m):
        component = table_finite_diff[m - (i // 2)][i] / math.factorial(i)  # индекс m-i соответствует индексу -i в формуле
        for j in range(i):
            if j % 2 == 0:
                component *= (t + ((j + 1) // 2))
            else:
                component *= (t - ((j + 1) // 2))
        polynom += component

    return polynom


def central_table_second_interpolation_formula_gauss(x_interpolation, xk_array):
    n = len(xk_array)
    h = xk_array[1] - xk_array[0]
    t = (x_interpolation - xk_array[0]) / h
    table_finite_diff = get_finite_difference_table(xk_array)

    m = n // 2
    if n % 2 == 0:
        m -= 1
    polynom = table_finite_diff[m][0]  # для y0 (который в формуле Гаусса - центральный элемент таблицы)
    for i in range(1, m):
        component = table_finite_diff[m - ((i + 1) // 2)][i] / math.factorial(i)  # индекс m-i соответствует индексу -i в формуле
        for j in range(i):
            if j % 2 == 0:
                component *= (t - ((j + 1) // 2))
            else:
                component *= (t + ((j + 1) // 2))
        polynom += component

    return polynom


def interpolation_polynom_equidistant_points(x_interpolation, xk_array):
    if x_interpolation < xk_array[1]:
        return start_table_interpolation_formula_newton(x_interpolation, xk_array)

    elif x_interpolation > xk_array[len(xk_array) - 1]:
        return end_table_interpolation_formula_newton(x_interpolation, xk_array)

    n = len(xk_array)
    m = n // 2
    if n % 2 == 0:
        m -= 1
    elif x_interpolation > xk_array[m]:
        return central_table_first_interpolation_formula_gauss(x_interpolation, xk_array)

    elif x_interpolation < xk_array[m]:
        return central_table_second_interpolation_formula_gauss(x_interpolation, xk_array)


def f(x):
    return 1 / (4 * x + x ** 3)


def main():
    # массив узлов интерполяции
    xk = [2.0, 2.3, 2.6, 2.9, 3.2]
    # точка, в которой нужно найти значение интерполяционного полинома
    x1 = 1.5
    x2 = 2.65

    polynomial1 = interpolation_polynom_equidistant_points(x1, xk)
    polynomial2 = interpolation_polynom_equidistant_points(x2, xk)
    f1 = f(x1)
    f2 = f(x2)

    print(f'Значение интерполяционного полинома в точке x={x1}:\n\t{polynomial1}')
    print(f'Фактическое значение функции в точке x={x1}:\n\t{f1}')
    print()
    print(f'Значение интерполяционного полинома в точке x={x2}:\n\t{polynomial2}')
    print(f'Фактическое значение функции в точке x={x2}:\n\t{f2}')


if __name__ == "__main__":
    main()
