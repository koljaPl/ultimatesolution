from sympy import symbols, solve, sqrt, Eq, sympify
from math import pow

#TODO проверь и перепроверь
def ArithmeticSolution():
    print("Ты выбрал арифмитическое вырожение.")
    example = str(input("Введите выражение: "))
    try:
        result = sympify(example)  # Преобразуем строку в математическое выражение
        print("Результат:", result)
    except Exception as e:
        print("Ошибка в выражении:", e)

#TODO cделай
def AlgebraicSolution():
    print("")

#TODO cделай
def TrigonometricSolution():
    print("")

#TODO cделай
def LogExpandSolution():
    print("")

#TODO cделай
def FractionsPercentsSolution():
    print("")

#TODO cделай
def DiffIntegrateSolution():
    print("")