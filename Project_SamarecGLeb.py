#Ініціалізація картки
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
#Ініціалізація переможних ліній
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


#Виведення картки на екран
def print_maps():
    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])


# Зробити хід у комірку
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Отримати поточний результат гри
def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Штучний інтелект: пошук лінії з необхідною кількістю X та O на переможних лініях
def check_line(sum_O, sum_X):
    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o = o + 1
            if maps[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]

    return step


# Штучний інтелект: вибір ходу
def AI():
    step = ""

    # 1) якщо на якійсь із переможних ліній 2 свої фігури та 0 чужих - ставимо
    step = check_line(2, 0)

    # 2) якщо на якійсь із переможних ліній 2 чужі фігури та 0 своїх - ставимо
    if step == "":
        step = check_line(0, 2)

        # 3) якщо 1 фігура своя та 0 чужих - ставимо
    if step == "":
        step = check_line(1, 0)

        # 4) центр порожній, то займаємо центр
    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5

            # 5) якщо центр зайнятий, то займаємо перший осередок
    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step


# Основна програма
game_over = False
human = True

while game_over == False:

    # 1. Показуємо картку
    print_maps()

    # 2. Запитаємо у того, хто грає, куди робити хід
    if human == True:
        symbol = "X"
        step = int(input("Людина, ваш хід: "))
    else:
        print("Комп'ютер робить хід: ")
        symbol = "O"
        step = AI()

    # 3. Якщо комп'ютер знайшов, куди зробити хід, то граємо. Якщо ні, то нічия.
    if step != "":
        step_maps(step, symbol)  # робимо хід у зазначений осередок
        win = get_result()  # визначимо переможця
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print("Нічія!")
        game_over = True
        win = "дружба"

    human = not (human)

# Гру закінчено. Покажемо картку. Оголосимо переможця.
print_maps()
print("Переміг", win)