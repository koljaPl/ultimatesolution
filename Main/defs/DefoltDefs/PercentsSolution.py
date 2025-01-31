from sympy import symbols, solve, sqrt, Eq, sympify, factorial, simplify

def parse_percent(expression: str):
    expression = expression.replace('%', '/100')  # Заменяем проценты
    return sympify(expression)

def solve_percent_equation(equation_str):
    equation_str = equation_str.replace('%', '/100')  # Заменяем проценты
    lhs, rhs = equation_str.split('=')  # Разделяем уравнение
    x = symbols('x')  # Создаем переменную
    eq = Eq(sympify(lhs), sympify(rhs))  # Создаем уравнение
    return solve(eq, x)  # Решаем

#TODO cделай
def PercentsSolution():
    print("Ты выбрал решать проценты. Ты хочешь решать проценты с x (Введите 1) или без (Введите 2)?")
    n = int(input("Введите число:"))
    try:
        if n == 1:
            try:
                example = str(input("Введите выражение: "))
                print("Ответ:", solve_percent_equation(example))  # [250]
            except Exception as e:
                print("Ошибка в выражении:", e)
                PercentsSolution()
        elif n == 2:
            example = str(input("Введите выражение без x: "))
            result = parse_percent(example).evalf(3)  # Преобразуем и вычисляем
            print("Ответ:", result)
        else:
            print("Ты ввел что-то не то, попробуй еще.")
            PercentsSolution()
    except Exception as e:
        print("Ошибка:", e)