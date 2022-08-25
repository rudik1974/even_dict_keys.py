library = {"name": "art"}

def add(name, art):
    s = {name: art}
    library.update(s)
    print(s)
    print(library)


def dell(name, art):
    if library.get(name) == None:
        print("Такого товару у каталозі не має, зробіть інший вибір!")
    else:
        s = {name: library.get(name)}
        print("Ви бажаєте видалити", s, "?")
        b = int(input("Натисніть 1, якщо ви дійсно бажаєте видалити цей товар:"))
        if b == 1:
            print("Ви видалили: ", library.pop(name))


while True:
    n = int(input("\n Оберіть пункт меню\n1 Переглянути повний каталог, \n2 Додати новий артикул, \n3 Видалити артикул"
                  "\n4 Вихід, \n Ваш вибір:"))
    if n == 1 or n == 2 or n == 3 or n == 4:
        if n == 4:
            break
        if n == 1:
            print("\nКаталог товарів: ", library)

        if n == 2:
            name = input("Введіть назву товару:")
            art = input("Введіть артикул товару:")
            add(name, art)


        if n == 3:
            name = input("Введіть назву товару: ")
            dell(name, art)
