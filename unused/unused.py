# НЕ РАБОЧИЙ КАЛ КОТОРЫЙ ЖАЛКО УДАЛИТЬ

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

user_input = input("Введите квадратное уравнение (например, x**2 - 5*x + 6 = 0): ")
eq = Eq(sympify(user_input.split("=")[0]), sympify(user_input.split("=")[1]))
solution = solve(eq, x)
print(f"Решения: {solution}")

x = symbols('x')
user_input = input("Введите уравнение (например, 2*x + 3 = 7): ")
eq = Eq(sympify(user_input.split("=")[0]), sympify(user_input.split("=")[1]))
solution = solve(eq, x)
print(f"Решение: {solution}")

user_input = input("Введите уравнение (например, x**4 - 5*x**2 + 4 = 0): ")
eq = Eq(sympify(user_input.split("=")[0]), sympify(user_input.split("=")[1]))
solution = solve(eq, x)
print(f"Решения: {solution}")
