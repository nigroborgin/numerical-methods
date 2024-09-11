import math

from sympy import Interval, Symbol, maximum, diff, minimum


def interpolation_polynomial_lagrange(x_interpolation, xk_array):
    polynom = 0.0
    n = len(xk_array)

    for k in range(n):
        numerator_of_fraction = 1
        denominator_of_fraction = 1

        for j in range(n):
            if j != k:
                numerator_of_fraction *= (x_interpolation - xk_array[j])
                denominator_of_fraction *= (xk_array[k] - xk_array[j])

        polynom += f(xk_array[k]) * (numerator_of_fraction / denominator_of_fraction)

    return polynom


def error_rate_of_formula(x_interpolation, xk_array):
    segment_start = min(min(xk_array), x_interpolation)
    segment_end = max(max(xk_array), x_interpolation)

    x = Symbol('x')
    f_expr = 1 / (4 * x + x ** 3)
    interval = Interval(segment_start, segment_end)
    # Нужна n+1 степень производной, n - индекс последнего элемента массива узлов интерполяции. Длина массива = n+1
    degree_derivative = len(xk_array)

    derivative = diff(f_expr, x, degree_derivative)
    max_of_derivative = maximum(derivative, x, interval)
    min_of_derivative = minimum(derivative, x, interval)
    max_of_derivative_of_the_abs = max(abs(max_of_derivative), abs(min_of_derivative))

    product_of_numbers = 1
    for i in range(len(xk_array)):
        product_of_numbers *= (x_interpolation - xk_array[i])

    return (max_of_derivative_of_the_abs / math.factorial(degree_derivative)) * (abs(product_of_numbers))


def f(x):
    return 1 / (4 * x + x ** 3)


def main():
    # массив узлов интерполяции
    xk = [2.0, 2.5, 3.0, 4.0]
    # точка, в которой нужно найти значение интерполяционного полинома
    x = 3.5

    polynomial = interpolation_polynomial_lagrange(x, xk)
    error_rate_of_formula_value = error_rate_of_formula(x, xk)
    reality_error_rate = abs(f(x) - polynomial)

    print(f'Значение интерполяционного полинома в точке x={x}:\n\t{polynomial}')
    print()
    print(f'Оценка погрешности формулы в точке x={x}\n\t{error_rate_of_formula_value}')
    print()
    print(f'Реальная погрешность:\n\t{reality_error_rate}')


if __name__ == "__main__":
    main()
