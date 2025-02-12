from sympy import sympify, sqrt, pi

# Парсер для красивых символов, такой парсер и в процентах и в арифметике
def parse_numbers(expression: str):
    """Парсит проценты и математические символы в понятный для SymPy формат"""
    replacements = {
        '%': '/100', '×': '*', '√': 'sqrt', '÷': '/',
        '−': '-', '²': '**2', '³': '**3', 'π': 'pi'
    }
    for old, new in replacements.items(): # Сам парсер
        expression = expression.replace(old, new) # Возвращает строку
    return expression # Вот тут проводиться решения выражения

# Тут функция по решению алгебраических выражений, очень интересно
def ArithmeticSolution():
    print("Ты выбрал арифметическое выражение.")
    example = str(input("Введите выражение: ")) # example переменная во всех дефах по решению
    try:
        result = sympify(parse_numbers(example).evalf(4)) # Преобразуем строку в математическое выражение\
        print("Результат:", result)
    except Exception as e:
        print("Ошибка в выражении:", e)
        ArithmeticSolution()

try:
    ArithmeticSolution()
except KeyboardInterrupt:
    print("\n\nПрограмма завершилась ручным выключением.")
except ValueError:
    print("\n\nТы ввел что-то не то.")
    ArithmeticSolution()