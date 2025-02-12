from Main.defs.malfunctions.LogExpandSolution import LogExpandSolution
from Main.defs.malfunctions.TrigonometricSolution import TrigonometricSolution
from Main.defs.malfunctions.DiffIntegrateSolution import DiffIntegrateSolution
from Main.defs.DefoltDefs.ArithmeticSolution import ArithmeticSolution
from Main.defs.DefoltDefs.AlgebraicSolution import AlgebraicSolution
from Main.defs.DefoltDefs.PercentsSolution import PercentsSolution
from Main.defs.Formuls.FormulMath import FormulMath
from Main.defs.Formuls.FormulPhisics import FormulPhisic
# from Main.defs.DefSolution import LogExpandSolution, FractionsPercentsSolution, DiffIntegrateSolution


#Сама главная функция с вызовами подфункций
def choose_solution():
    print("Выберите какой пример хотите решать:\n"
    " (1) Для решения арифметических выражений нажмите 1 \n",
    "(2) Для решения сложных алгебраических уравнений () нажмите 2 \n",
    "(3) Для решения процентов нажмите 3\n",
    "(4) Для решения логарифмов и экспонентов нажмите 4 НЕРАБОТАЕТ\n",
    "(5) Для решения тригонометрических уравнений и/или выражений нажмите 3 НЕРАБОТАЕТ \n",
    "(6) Для выбора дифференцирование и интегрирование нажмите 6 НЕРАБОТАЕТ\n",)
    n = int(input("Введи какой тип примера хочешь решать: "))
    if n == 1:
        ArithmeticSolution()    # Вызывает функцию по решению арифметических выражений                      РАБОТАЕТ
    elif n == 2:
        AlgebraicSolution()     # Вызывает функцию по решению алгебраических выражений                      ПОКА НЕ РАБОТАЕТ
    elif n == 3:
        PercentsSolution()      # Вызывает функцию по решению процентов с x и без                           РАБОТАЕТ
    elif n == 4:
        LogExpandSolution()     # Вызывает функцию по решению логарифмов и экспонентов                      НЕ РАБОТАЕТ
    elif n == 5:
        TrigonometricSolution() # Вызывает функцию по решению тригонометрических уравнений и/или выражений  НЕ РАБОТАЕТ И СКОРЕЕ ВСЕГО НЕ БУДЕТ
    elif n == 6:
        DiffIntegrateSolution() # Вызывает функцию по решению дифференцирование и интегрирование            НЕ РАБОТАЕТ
    else:
        print("Ты не нато нажал.")
        choose_solution() # Перезапуск функции если пользователь ввел не ту цифру

# Функция выбора
def choose_what():
    print("Привет, это программа с универсальными решениями, что ты хочешь решать,"
          "математику с арифметикой и алгеброй (нажми 1) или посмотреть формулы для математики и физики (нажми 2)?")
    n = int(input("Что хочешь решать: "))
    if n == 1:
        try:
            choose_solution()
        except KeyboardInterrupt:
            print("\n\nПрограмма завершилась ручным выключением.")
        except ValueError:
            print("\n\nТы ввел что-то не то.")
            choose_solution()
    elif n == 2:
        print("Ты выбрал формулы, для чего формулу ты хочешь решать? математика - (1), физика - (2)")
        n = int(input("Что хочешь решать: "))
        if n == 1:
            FormulPhisic()
        elif n == 2:
            FormulMath()
    else:
        print("Ты не нато нажал.")
        choose_what() # Перезапуск функции если пользователь ввел не ту цифру

#Вызов главной функции
try:
    choose_what()
except KeyboardInterrupt:
    print("\n\nПрограмма завершилась ручным выключением.")
except ValueError:
    print("\n\nТы ввел что-то не то.")
    choose_what()