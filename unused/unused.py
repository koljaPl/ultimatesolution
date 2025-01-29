
def LinealSolution():
    print("Ты выбрал линейные или ниленейные функции.")
    inequality = str(input())
    x = symbols('x')
    solution = solve(inequality, x)
    print("Ответ:", solution)

#inequality = str(input())

# Определяем переменные
#x = symbols('x')

# Задаем неравенство 2 / sqrt((x - sqrt(3) * sqrt(3) - 2 * x + 1)) = g(x)
#inequality = (4 - sqrt(17)) * (3 * x + 5) >= 0

# Решаем неравенство
#solution = solve(inequality, x)

# Выводим результат
#print("Решение:", solution)
