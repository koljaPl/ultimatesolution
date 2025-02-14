from sympy import symbols, solve, sqrt, Eq, sympify, factorial, simplify
import re
from math import pow

# Парсер для красивых символов, такой парсер и в процентах и в арифметике
def parse_numbers(expression: str):
    """Парсит проценты и математические символы в понятный для SymPy формат"""
    replacements = {
        '%': '/100', '×': '*', '√': 'sqrt', '÷': '/',
        '−': '-', '²': '**2', '³': '**3', 'π': 'pi'
    }
    for old, new in replacements.items(): # Сам парсер
        expression = expression.replace(old, new)
    expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)    # Исправляем 3x → 3*x (если перед x стоит цифра, но нет оператора *)
    expression = re.sub(r'(\d)\(', r'\1*(', expression)     # Исправляем 4(x+2) → 4*(x+2) (если перед скобкой число, но нет оператора *)
    expression = re.sub(r'\)\(', r')*(', expression)     # Исправляем (2x+5)(x-3) → (2x+5) * (x-3) (если две скобки идут подряд)
    expression = expression.replace(" ", "")    # Убираем лишние пробелы (чтобы sympify() не ломался)
    return expression # Возвращаем отформатированное выражение

    #TODO Я ЗАКОНЧИЛ СВОЮ ПРОВЕРКУ НА 27 УРАВНЕНИИ (x - 2)(x + 4) = 15, в нем все перестало работать, дальше не знаю, еще нужно добавить обратный парсер,
    # то есть когда программа отдает ответ нужно все обратно перепарсить в красивые числа

# Функция по решению Линейные уравнения
def LinearSolution():
    """Решает линейные уравнения"""
    print("Ты выбрал линейные выражений, введи что нужно найти (букву, если не введете будет выбрана стандартная буква x) и конечно же свое выражение.")
    letter = input("Введите букву: ").strip() or "x" # Добавил дефолтное значение и убираем пробелы
    # Проверяем, что переменная состоит только из букв
    if not letter.isalpha():
        print("Ошибка: переменная должна содержать только буквы.")
        return None
    x = symbols(letter)  # Создаем переменную
    example = str(input("Введите выражение: ")).strip() # Если берем выражение и убираем пробелы
    try:
        parsed_example = parse_numbers(example)
        if "=" not in parsed_example:      # Разделяем левую и правую часть уравнения
            raise ValueError("Уравнение должно содержать знак '='.")
        left_side = sympify(parsed_example.split("=")[0])  ### Разделает эти две части, эта строка и следующая
        right_side = sympify(parsed_example.split("=")[1]) ### Эти 3 строки являются заменителем этой страшной строки - eq = Eq(sympify(parsed_example.split("=")[0]), sympify(ParsedExample.split("=")[1]))
        eq = Eq(left_side, right_side)                     ###
        solution = solve(eq, x) # Решает выражение
        return solution
    except Exception as e:
        print(f"Ошибка: {e}. Проверьте правильность ввода.")
        return None  # Возвращаем None в случае ошибки


# Функция с неравенствами
def Inequality():
    print("Ты выбрал решение неравенства, выбери что ты хочешь решать: ")


#TODO cделай потому что ничиго не работает
def AlgebraicSolution():
    print("Ты выбрал алгебраическое выражение, но тебе предстоит еще 1 выбор между: \n  - Линейными уравнениями (1) \n  - Квадратными уравнениями (2) ",
          "\n  - Уравнениями высших степеней (3) \n  - Системой линейных уравнений (4) \n  - Неравенства (5)")
    n = int(input("Введите что вы хотите выбрать: "))
    if n == 1:
        try:
            solution = LinearSolution()
            if solution is not None:
                print("Ответ:", solution)
        except Exception as e:
            print("Ошибка в выражении:", e)
            solution1 = LinearSolution()
            print("Ответ:", solution1)
    elif n == 2:
        # TODO доделай
        print("Ты выбрал квадратные уравнения.")
        example = str(input("Введите выражение: "))
    elif n == 3:
        # TODO доделай
        print("Ты выбрал уравнения высших степеней.")
        example = str(input("Введите выражение: "))
    elif n == 4:
        # TODO доделай
        print("Ты выбрал системы линейных уравнений.")
        example = str(input("Введите выражение: "))
    elif n == 5:
        # TODO доделай
        print("Ты выбрал неравенства.")
        example = str(input("Введите выражение: "))
    else:
        print("Ты ввел что-то не то.")
        AlgebraicSolution()


try:
    AlgebraicSolution()
except KeyboardInterrupt:
    print("\n\nПрограмма завершилась ручным выключением.")
except ValueError:
    print("\n\nТы ввел что-то не то.")
    AlgebraicSolution()