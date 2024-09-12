# from sympy import Symbol
import matplotlib.pyplot as plt
import numpy as np


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


# функция для полноценного метода половинного деления
def method_division_into_two(x_1: float, x0: float, l: float):
    x_star: float
    while abs(x_1 - x0) > l:
        y = (x0 + x_1) / 2
        if f(x_1) * f(y) < 0:
            x0 = y
        elif f(x0) * f(y) < 0:
            x_1 = y
        else:
            x_star = y
            return [0.0, x_star]
    return [1.0, x_1, x0]


# функция для нескольких итераций метода половинного деления
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
            return [0.0, x_star]
    return [1.0, x_1, x0]


def draw_graph_of_function(x_left, x_right, step, title):
    x_coords = np.arange(x_left, x_right, step)
    y_coords = []
    for i in x_coords:
        y_coords.append(f(i))
    plt.title(title)
    plt.xlabel('x', color='gray')
    plt.ylabel('y', color='gray')
    plt.grid(True)
    plt.plot(x_coords, y_coords)
    plt.show()


def f(x):
    return x**3 + 3*x - 7


def main():
    # x = Symbol('x')
    # f_expr = x**3 + 3*x - 7

# 1. рисуем график функции с помощью matplotlib.pyplot (для дальнейшего вывода на консоль, надо закрыть окно с графиком)
    draw_graph_of_function(-5, 5, 0.1, r'$y = x^3 + 3x -7$')

    # при просмотре графика видим какой отрезок лучше использовать:
    x_1 = -2.0
    x0 = 2.0
    # длина отрезка, в котором должен находиться искомый X*
    l = 0.1

    # функция для полноценного метода половинного деления
    # result_list = method_division_into_two(x_1, x0, l)

# 2. функция для нескольких (двух) итераций метода половинного деления
    result_list = method_division_into_two__with_count_iterations(x_1, x0, l, 2)

    # result_list[0] = 0 - X* найдено
    if result_list[0] == 0.0:
        # (для вывода на консоль, надо закрыть окно с графиком)
        print(f'Искомая точка: x={result_list[1]}')
    # result_list[0] = 1 - найден отрезок [x_1, x0] нужной длины
    elif result_list[0] == 1.0:
        x_1 = result_list[1]
        x0 = result_list[2]

# 3. функция для нескольких (трёх) итераций метода секущих
        result = method_secant(x_1, x0, 3)
        # (для вывода на консоль, надо закрыть окно с графиком)
        print(f'Искомая точка: x={result}')


if __name__ == "__main__":
    main()
