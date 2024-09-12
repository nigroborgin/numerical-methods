import numpy as np


# Функция F' для вычисления градиента
def gradient(A, x, b):
    return A.T @ (A @ x - b)


def main():
    A = np.array([[5.0, 4.0, 1.0],
                  [4.0, 6.0, 3.0],
                  [6.0, 5.0, 2.0]])
    b = np.array([-2.0, -6.0, -5.0])
    x = np.array([0.0, 1.0, -3.5])
    iterations = 5
    delta = 0.01

    for i in range(iterations):
        grad = gradient(A, x, b)

        # Вычисляем динамический шаг λ_k
        numerator = np.dot(grad, grad)
        denominator = np.dot(A @ grad, A @ grad)
        if denominator == 0:  # Предотвращаем деление на 0
            print("Деление на 0, остановка итераций.")
            break
        lambda_k = numerator / denominator

        # Обновляем значение x
        x_new = x - lambda_k * grad

        # Проверка на точность
        if np.linalg.norm(A @ x_new - b) < delta:
            print(f"Достигнута точность на итерации {i + 1}: x = {x_new}")
            break

        # Переход к следующей итерации
        x = x_new
        print(f"Итерация {i + 1}: x = {x}")

    print("Решение:", x)

if __name__ == "__main__":
    main()
