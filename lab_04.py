import math

from sympy import Symbol, diff


def get_difference_ratio_table(xk_array):
    n = len(xk_array)
    table_diff_ratio = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        table_diff_ratio[i][0] = f(xk_array[i])

    for j in range(1, n):
        for i in range(j, n):
            table_diff_ratio[i][j] = (table_diff_ratio[i][j - 1] - table_diff_ratio[i - 1][j - 1]) / \
                        (xk_array[i] - xk_array[i - j])

    return table_diff_ratio


def numerical_differentiation(x_interpolation, xk_array, m):
    n = len(xk_array)
    if m > n:
        return 0
    table_diff_ratio = get_difference_ratio_table(xk_array)

    ak_array = [0]*n
    for i in range(n):
        ak_array[i] = (x_interpolation - xk_array[i])

    # первое слагаемое в формуле приближённой производной степени m
    derivative = table_diff_ratio[m][m]
    component = 1
    for i in range(m):
         component += ak_array[i]
    # второе слагаемое
    derivative += table_diff_ratio[m + 1][m + 1] * component

    # все остальные слагаемые считаем по общей формуле
    for i in range(m + 2, n):

        sum_for_component = ak_array[0] * ak_array[1]
        # j идёт от 2 до i-1. изначально i = m+2
        for j in range(2, i):
            sum_for_component += ak_array[j - 2] * ak_array[j - 1]
            sum_for_component += ak_array[j - 2] * ak_array[j]
        component = table_diff_ratio[i][i] * sum_for_component
        derivative += component

    derivative *= math.factorial(m)
    return derivative


def f(x):
    return 1 / (4 * x + x ** 3)


def main():
    # массив узлов интерполяции
    xk = [2.0, 2.3, 2.6, 2.9, 3.2]
    # точка, в которой нужно найти значение интерполяционного полинома
    x1 = 1.5
    x2 = 2.65

    # вычисление приближённых значений производных с помощью численного дифференцирования
    derivative1_x1 = numerical_differentiation(x1, xk, 1)
    derivative1_x2 = numerical_differentiation(x2, xk, 1)
    derivative2_x1 = numerical_differentiation(x1, xk, 2)
    derivative2_x2 = numerical_differentiation(x2, xk, 2)

    # вычисление значений производных с помощью библиотечной функции
    x = Symbol('x')
    f_expr = 1 / (4 * x + x ** 3)
    dx_f1_x1 = diff(f_expr, x, 1).evalf(subs={x: x1})
    dx_f1_x2 = diff(f_expr, x, 1).evalf(subs={x: x2})
    dx_f2_x1 = diff(f_expr, x, 2).evalf(subs={x: x1})
    dx_f2_x2 = diff(f_expr, x, 2).evalf(subs={x: x2})

    print(f'Приближённое значение Первой производной в точке x={x1}:\n\t{derivative1_x1}')
    print(f'Точное значение Первой производной в точке x={x1}:\n\t{dx_f1_x1}')
    print()
    print(f'Приближённое значение Первой производной в точке x={x2}:\n\t{derivative1_x2}')
    print(f'Точное значение Первой производной в точке x={x2}:\n\t{dx_f1_x2}')
    print()
    print(f'Приближённое значение Второй производной в точке x={x1}:\n\t{derivative2_x1}')
    print(f'Точное значение Второй производной в точке x={x1}:\n\t{dx_f2_x1}')
    print()
    print(f'Приближённое значение Второй производной в точке x={x2}:\n\t{derivative2_x2}')
    print(f'Точное значение Второй производной в точке x={x2}:\n\t{dx_f2_x2}')


if __name__ == "__main__":
    main()
