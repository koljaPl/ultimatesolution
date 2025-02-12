from sympy import symbols, solve, sqrt, Eq, sympify, factorial, simplify, pi

# Парсер для красивых чисел для питона /
def parse_percent(expression: str):
    """Парсит проценты и математические символы в понятный для SymPy формат."""
    replacements = {
        '%': '/100', '×': '*', '√': 'sqrt', '÷': '/',
        '−': '-', '²': '**2', '³': '**3', 'π': 'pi'
    }
    for old, new in replacements.items():
        expression = expression.replace(old, new)
    return sympify(expression)

# Не парсер, но тоже интересно, решает задачи для уравнений процентов с x
def solve_percent_equation(equation_str):
    equation_str = equation_str.replace('%', '/100')  # Заменяем проценты
    lhs, rhs = equation_str.split('=')  # Разделяем уравнение
    x = symbols('x')  # Создаем переменную
    eq = Eq(sympify(lhs), sympify(rhs))  # Создаем уравнение
    return solve(eq, x)  # Решаем

# Функция по решению процентов
def PercentsSolution():
    print("Ты выбрал решать проценты. Ты хочешь решать проценты с x (Введите 1) или без (Введите 2)?")
    n = int(input("Введите число:"))
    try:
        if n == 1:
            try: # C x
                example = str(input("Введите выражение: "))
                print("Ответ:", solve_percent_equation(example))  # [250]
            except Exception as e:
                print("Ошибка в выражении:", e)
                PercentsSolution()
        elif n == 2: # без x
            example = str(input("Введите выражение без x: "))
            result = parse_percent(example).evalf(4)  # Преобразуем и вычисляем
            print("Ответ:", result)
        else:
            print("Ты ввел что-то не то, попробуй еще.")
            PercentsSolution()
    except Exception as e:
        print("Ошибка:", e)


try:
    PercentsSolution()
except KeyboardInterrupt:
    print("\n\nПрограмма завершилась ручным выключением.")
except ValueError:
    print("\n\nТы ввел что-то не то.")
    PercentsSolution()