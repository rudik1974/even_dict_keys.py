import math

def addition():
    print("ви обрали Додавання")
    a = float(input("введіть перший доданок:"))
    b = float(input("введіть другий доданок:"))
    print("\n", a, "+", b, "=", round(a + b, 3), sep="")


def subtraction():
    print("ви обрали Віднімання")
    a = float(input("введіть зменшуване:"))
    b = float(input("введіть від'ємник:"))
    print("\n", a, "-", b, "=", round(a - b, 3), sep="")


def mult():
    print("ви обрали Множення")
    a = float(input("введіть перший множник:"))
    b = float(input("введіть другий множник:"))
    print("\n", a, "*", b, "=", round(a * b, 3), sep="")


def div():
    print("ви обрали Ділення")
    a = float(input("введіть ділене:"))
    b = float(input("введіть дільник, який не дорівнює нулю:"))
    if b == 0:
        print("Дільник не може дорівнювати нулю!")
        b = float(input("введіть дільник, який не дорівнює нулю:"))
        print("\n", a, "/", b, "=", round(a / b, 3), sep="")
    else:
        print("\n", a, "/", b, "=", round(a / b, 3), sep="")


def exp():
    print("ви обрали Зведення в ступінь")
    a = float(input("введіть основу:"))
    b = float(input("введіть ступінь:"))
    print("\n", a, "^", b, "=", round(a ** b, 3), sep="")


def sq_root():
    print("ви обрали Квадратний корінь")
    a = float(input("введіть підкореневий вираз:"))
    print("\n", "Корінь квадратний з ", a, "=", round(a ** (1 / 2), 3), sep="")


def cub_root():
    print("ви обрали Кубічний корінь")
    a = float(input("введіть підкореневий вираз:"))
    print("\n", "Корінь кубічний з ", a, "=", round(a ** (1 / 3), 3), sep="")

def sinus():
    print("ви обрали Синус")
    a = float(input("введіть підкореневий вираз:"))
    print("\n", "Синус з ", a, "=", round(math.sin(a)), sep="")


while True:
    n = int(input("\n Оберіть пункт меню\n1 Додавання, \n2 Віднімання, \n3 Множення, \n4 Ділення"
                  "\n5 Піднесення до степеня, \n6 Корінь квадратний, \n7 Корінь кубічний,\n8 Синус, \n Ваш вибір:"))
    if n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7 or n == 8:
        if n == 9:
            break
        if n == 1:
            addition()

        if n == 2:
            subtraction()

        if n == 3:
            mult()

        if n == 4:
            div()

        if n == 5:
            exp()

        if n == 6:
            sq_root()

        if n == 7:
            cub_root()

        if n == 8:
            sinus()


