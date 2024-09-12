from sympy import Symbol, diff


def method_division_into_two__with_count_iterations(x_1: float, x0: float, l: float, count_iterations: int):
    x_star = None
    for i in range(count_iterations):
        if abs(x_1 - x0) < l:
            break

        y = (x0 + x_1) / 2
        if f(x_1) * f(y) < 0:
            x0 = y
        elif f(x0) * f(y) < 0:
            x_1 = y
        else:
            x_star = y
            # result_list[0] = 0 - X* найдено
            return [0.0, x_star]
    # result_list[0] = 1 - найден отрезок [x_1, x0] нужной длины
    return [1.0, x_1, x0]


# функция для нескольких итераций метода секущих
def method_secant(xn_1: float, xn: float, count_iterations: int):
    xn1: float
    for i in range(count_iterations):
        fxn = f(xn)
        fxn_1 = f(xn_1)
        xn1 = (xn_1 * fxn - xn * fxn_1) / (fxn - fxn_1)
        xn_1 = xn
        xn = xn1
    return xn1


def method_newton(xn: float, count_iterations: int, f_expr, x):
    xn1: float
    for i in range(count_iterations):
        fxn = f(xn)
        fxn_derivative = diff(f_expr, x, 1).evalf(subs={x: xn})
        xn1 = xn - fxn / fxn_derivative
        xn = xn1
    return xn1


def f(x: float):
    return x ** 3 + 3 * x - 7


def main():
    x = Symbol('x')
    f_expr = x ** 3 + 3 * x - 7

    # при просмотре графика видим какой отрезок лучше использовать:
    x_1 = -2.0
    x0 = 2.0
    # длина отрезка, в котором должен находиться искомый X*
    l = 0.1

# 1. функция для нескольких (двух) итераций метода половинного деления
    result_list = method_division_into_two__with_count_iterations(x_1, x0, l, 2)
    # result_list[0] = 0 - X* найдено
    if result_list[0] == 0.0:
        print(f'Искомая точка: x={result_list[1]}')
    # result_list[0] = 1 - найден отрезок [x_1, x0] нужной длины
    elif result_list[0] == 1.0:
        x_1 = result_list[1]
        x0 = result_list[2]
        # функция для нескольких (трёх) итераций метода Секущих
        result_secant = method_secant(x_1, x0, 3)
        # функция для нескольких (трёх) итераций метода Ньютона
        result_newton = method_newton(x_1, 3, f_expr, x)
# 2. сравнение результатов методов Секущих и Ньютона
        print(f'Искомая точка по методу Секущих: x={result_secant}')
        print(f'Искомая точка по методу Ньютона: x={result_newton}')
        # взято из построения графика в Desmos: https://www.desmos.com/Calculator?lang=ru
        fact_point = 1.406288
        print(f'Фактическая точка пересечения графика оси x: {fact_point}')
# Вывод: метод Ньютона оказался более точным
        print('Вывод: метод Ньютона оказался более точным')


if __name__ == "__main__":
    main()
