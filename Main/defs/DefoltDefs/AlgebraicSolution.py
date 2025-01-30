from sympy import symbols, solve, sqrt, Eq, sympify, factorial, simplify
from math import pow

#TODO cделай потому что нихуя не работает
def AlgebraicSolution():
    print("Ты выбрал алгебраическое вырожение, но тебе предстоит еще 1 выбор между: \n  - Линейными уравнениями (1) \n  - Квадратными уравнениями (2) ",
          "\n  - Уравнениями высших степеней (3) \n  - Системой линейных уравнений (4) \n  - Неравенства (5)")
    n = int(input("Введите что вы хотите выбрать: "))
    if n == 1:
        #TODO доделай
        print("Ты выбрал линейные уравнения.")
        example = str(input("Введите выражение: "))
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