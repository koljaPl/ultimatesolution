from sympy import symbols, solve, sqrt, Eq
from math import pow
from DefSolution import ArithmeticSolution, AlgebraicSolution, TrigonometricSolution
from DefSolution import LogExpandSolution, FractionsPercentsSolution, DiffIntegrateSolution

def choose_solution():
    print("Выбирите какой пример хотите решать:\n"
    " (1) Для решения арифметических выражений нажмите 1 \n",
    "(2) Для решения алгебраических уравнений нажмите 2 \n",
    "(3) Для решения тригонометрических уравнений и/или выражений нажмите 3 \n",
    "(4) Для решения логарифмов и экспонентов нажмите 4 \n",
    "(5) Для решения дробей и процентов нажмите 5 \n",
    "(6) Для выбора дифференцирование и интегрирование нажмите 6 \n",)
    n = int(input("Введи какой тип примера хочешь решать:"))
    if n == 1:
        print("1")
        ArithmeticSolution()
    elif n == 2:
        AlgebraicSolution()
    elif n == 3:
        TrigonometricSolution()
    elif n == 4:
        LogExpandSolution()
    elif n == 5:
        FractionsPercentsSolution()
    elif n == 6:
        DiffIntegrateSolution()
    else:
        print("Ты не нато нажал.")

choose_solution()
#TODO сделай так чтобы при конце работы приложения небыло ошибки, скорее всего через try except
