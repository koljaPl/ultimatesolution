from Main.defs.malfunctions.LogExpandSolution import LogExpandSolution
from Main.defs.malfunctions.TrigonometricSolution import TrigonometricSolution
from Main.defs.malfunctions.DiffIntegrateSolution import DiffIntegrateSolution
from Main.defs.DefoltDefs.ArithmeticSolution import ArithmeticSolution
from Main.defs.DefoltDefs.AlgebraicSolution import AlgebraicSolution
from Main.defs.DefoltDefs.PercentsSolution import PercentsSolution
#from Main.defs.DefSolution import ArithmeticSolution, TrigonometricSolution
#from Main.defs.DefSolution import LogExpandSolution, FractionsPercentsSolution, DiffIntegrateSolution

#Сама главная функция с вызовами подфункций
def choose_solution():
    print("Выбирите какой пример хотите решать:\n"
    " (1) Для решения арифметических выражений нажмите 1 \n",
    "(2) Для решения сложных алгебраических уравнений нажмите 2 \n",
    "(3) Для решения тригонометрических уравнений и/или выражений нажмите 3 НЕРАБОТАЕТ\n",
    "(4) Для решения логарифмов и экспонентов нажмите 4 НЕРАБОТАЕТ\n",
    "(5) Для решения процентов нажмите 5 \n",
    "(6) Для выбора дифференцирование и интегрирование нажмите 6 НЕРАБОТАЕТ\n",)
    n = int(input("Введи какой тип примера хочешь решать:"))
    if n == 1:
        ArithmeticSolution()
    elif n == 2:
        AlgebraicSolution()
    elif n == 3:
        TrigonometricSolution()
    elif n == 4:
        LogExpandSolution()
    elif n == 5:
        PercentsSolution()
    elif n == 6:
        DiffIntegrateSolution()
    else:
        print("Ты не нато нажал.")
        choose_solution()

#Вызов главной функции
try:
    choose_solution()
except KeyboardInterrupt:
    print("\n\nПрограмма завершилась ручным выключением.")
except ValueError:
    print("\n\nТы ввел что-то не то.")
    choose_solution()