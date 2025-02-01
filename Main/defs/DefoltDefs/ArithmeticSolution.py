from sympy import sympify

# Тут функция по решению алгебраических выражений, очень интерестно
def ArithmeticSolution():
    print("Ты выбрал арифмитическое вырожение.")
    example = str(input("Введите выражение: ")) # example переменная во всех дефах по решению
    try:
        result = sympify(example)  # Преобразуем строку в математическое выражение
        print("Результат:", result)
    except Exception as e:
        print("Ошибка в выражении:", e)
        ArithmeticSolution()
