from sympy import sympify
from math import pow

def ArithmeticSolution():
    print("Ты выбрал арифмитическое вырожение.")
    example = str(input("Введите выражение: "))
    try:
        result = sympify(example)  # Преобразуем строку в математическое выражение
        print("Результат:", result)
    except Exception as e:
        print("Ошибка в выражении:", e)
        ArithmeticSolution()
