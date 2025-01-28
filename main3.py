from sympy import symbols, sqrt, solve, Eq, And


def solve_case(inequality_str: str):
    x = symbols('x')  # Определяем переменную x

    # Преобразуем строку в выражение
    inequality = eval(inequality_str)

    if isinstance(inequality, (Eq, bool)):
        # Если это уравнение или логическое выражение, решаем его
        solution = solve(inequality, x)
        return solution
    else:
        # Если это выражение, проверяем его область определения
        # Условие 1: знаменатель не равен 0
        denominator = inequality.as_numer_denom()[1]  # Получаем знаменатель
        denominator_not_zero = solve(Eq(denominator, 0), x)

        # Условие 2: подкоренное выражение (если есть корень) ≥ 0
        if denominator.has(sqrt):
            radicand = denominator.args[0]  # Получаем подкоренное выражение
            inequality_solution = solve(radicand >= 0, x)
        else:
            inequality_solution = None

        return {
            "Область определения (знаменатель ≠ 0)": denominator_not_zero,
            "Область определения (подкоренное выражение ≥ 0)": inequality_solution
        }


# Запрашиваем ввод от пользователя
print(
    "Введите пример для решения (например, '2 / sqrt((x - sqrt(3))**2 - 2 * x + 1)' или '(4 - sqrt(17)) * (3 * x + 5) >= 0'):")
inequality_input = input()

# Решаем пример
try:
    solution = solve_case(inequality_input)
    print("Решение:", solution)
except Exception as e:
    print("Ошибка при обработке примера:", e)
