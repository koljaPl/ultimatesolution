from sympy import sympify, sqrt, pi

# Парсер для красивых символов
def parse_numbers(expression: str):
    """Парсит проценты и математические символы в понятный для SymPy формат"""
    replacements = {
        '%': '/100', '×': '*', '√': 'sqrt', '÷': '/',
        '−': '-', '²': '**2', '³': '**3', 'π': 'pi'
    }
    for old, new in replacements.items(): # Сам парсер
        expression = expression.replace(old, new)
    return sympify(expression) # Вот тут проводиться решения выражения

# Тут функция по решению алгебраических выражений, очень интерестно
def ArithmeticSolution():
    print("Ты выбрал арифмитическое вырожение.")
    example = str(input("Введите выражение: ")) # example переменная во всех дефах по решению
    try:
        result = parse_numbers(example).evalf(4) # Преобразуем строку в математическое выражение\
        print("Результат:", result)
    except Exception as e:
        print("Ошибка в выражении:", e)
        ArithmeticSolution()
