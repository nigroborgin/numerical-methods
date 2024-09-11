from sympy import Interval, Symbol, maximum, minimum, diff, lambdify


def integral_trapezoid(a, b, n):
    h = (b - 1) / n
    integral = ((b - a) / n)

    component = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        component += f(a + i * h)
    integral *= component

    return integral


def integral_parabola(a, b, n):
    h = (b - 1) / n
    integral = (b - a) / (6 * n)
    macro_component = f(a) + f(b)
    micro_component1 = 0
    micro_component2 = 0

    for i in range(1, n):
        micro_component1 += f(a + i*h)
    micro_component1 *= 2

    for i in range(1, n+1):
        micro_component2 += f(a + (2*i-1)*h/2)
    micro_component2 *= 4

    macro_component += micro_component1 + micro_component2
    integral *= macro_component

    return integral


def error_rate_of_formula_trapezoid(a, b, n):
    x = Symbol('x')
    f_expr = 1 / (4 * x + x ** 3)
    interval = Interval(a, b)
    derivative = diff(f_expr, x, 2)
    max_of_derivative = maximum(derivative, x, interval)
    min_of_derivative = minimum(derivative, x, interval)
    max_of_derivative_of_the_abs = max(abs(max_of_derivative), abs(min_of_derivative))

    r = - ((b - a) / n**2) * (max_of_derivative_of_the_abs / 12)
    return r


def error_rate_of_formula_parabola(a, b, n):
    x = Symbol('x')
    f_expr = 1 / (4 * x + x ** 3)
    interval = Interval(a, b)
    derivative = diff(f_expr, x, 4)
    max_of_derivative = maximum(derivative, x, interval)
    min_of_derivative = minimum(derivative, x, interval)
    max_of_derivative_of_the_abs = max(abs(max_of_derivative), abs(min_of_derivative))

    r = - ((b - a)**5 * max_of_derivative_of_the_abs) / (6*n)
    return r


def f(x):
    return 1 / (4 * x + x ** 3)


def main():
    a = 7
    b = 8
    n = 5

    integral_trapezoid_value = integral_trapezoid(a, b, n)
    integral_parabola_value = integral_parabola(a, b, n)
    error_rate_trapezoid_value = error_rate_of_formula_trapezoid(a, b, n)
    error_rate_parabola_value = error_rate_of_formula_parabola(a, b, n)

    x = Symbol('x')
    f_expr = 1 / (4 * x + x ** 3)
    integral_function = lambdify(x, f_expr)
    definite_integral = integral_function(b) - integral_function(a)

    print(f'Приближённое значение интеграла по формуле Трапеции [a, b]=[{a}, {b}], n={n}:\n\t{integral_trapezoid_value}')
    print(f'Приближённое значение интеграла по формуле Параболы [a, b]=[{a}, {b}], n={n}:\n\t{integral_parabola_value}')
    print(f'Точное значение интеграла [a, b]=[{a}, {b}], n={n}:\n\t{definite_integral}')
    print()
    print(f'Оценка погрешности численного интегрирования для формулы Трапеции [a, b]=[{a}, {b}], n={n}:\n\t{error_rate_trapezoid_value}')
    print(f'Оценка погрешности численного интегрирования для формулы Параболы [a, b]=[{a}, {b}], n={n}:\n\t{error_rate_parabola_value}')


if __name__ == "__main__":
    main()
