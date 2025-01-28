from sympy import symbols, solve, sqrt, Eq
from math import pow

#TODO сделай плис racionalSOLUTION и дополни
#def racionalSOLUTION():
#   print("Ты выбрал рациональные функции.")

#TODO сделай плис LinealSolution и дополни
#def LinealSolution():
#   print("Ты выбрал линейные или ниленейные функции.")

def choose_solution():
    print("Выбирите какой пример хотите решать:\n (1) Примеры работы с рациональными функциеми с квадратным корнем в знаменателе.",
          "Для ответа напишите 1\n (2) Пример решения линейного или нелинейного неравенства. Для ответа напишите 2")
    n = int(input())
    if n == 1:
        #racionalSOLUTION()
    elif n == 2:
        #LinealSolution()
    else:
        print("Ты не нато нажал.")
inequality = str(input())

# Определяем переменные
x = symbols('x')

# Задаем неравенство 2 / sqrt((x - sqrt(3) * sqrt(3) - 2 * x + 1)) = g(x)
#inequality = (4 - sqrt(17)) * (3 * x + 5) >= 0

# Решаем неравенство
solution = solve(inequality, x)

# Выводим результат
print("Решение:", solution)