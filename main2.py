from sympy import symbols, solve, sqrt

# Определяем переменные
x = symbols('x')

# Задаем неравенство
inequality = (4 - sqrt(17)) * (3 * x + 5) >= 0

# Решаем неравенство
solution = solve(inequality, x)

# Выводим результат
print("Решение:", solution)
