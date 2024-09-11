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


def interpolation_polynomial_newton(x_interpolation, xk_array):
    n = len(xk_array)
    table_diff_ratio = get_difference_ratio_table(xk_array)

    polynom = table_diff_ratio[0][0]
    for i in range(1, n):
        component = table_diff_ratio[i][i]
        for j in range(i):
            component *= (x_interpolation - xk_array[j])
        polynom += component

    return polynom


def f(x):
    return 1 / (4 * x + x ** 3)


def main():
    # массив узлов интерполяции
    xk = [2.0, 2.5, 3.0, 4.0]
    # точка, в которой нужно найти значение интерполяционного полинома
    x = 3.5
    polynomial = interpolation_polynomial_newton(x, xk)
    print(f'Значение интерполяционного полинома в точке x={x}:\n\t{polynomial}')


if __name__ == "__main__":
    main()
