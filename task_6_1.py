def start_game():
    print("Игра 'Крестики - Нолики'")
    print("Для игры необходимо вводить x и y")
    print("x - номер строки")
    print("y - номер столбца")
    print()


field = [[' '] * 3 for i in range(3)]


def playground():
    print("  | 0 | 1 | 2 |")
    print('---------------')
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("---------------")


def req_coordinates():
    print("Введите координаты")
    while True:
        coordinate = input("Координаты: ").split()
        if len(coordinate) != 2:
            print("Необходимо ввести две координаты.")
        else:
            x, y = coordinate
            if x.isdigit() and y.isdigit():
                x, y = int(x), int(y)
                if 0 <= x <= 2 and 0 <= y <= 2:
                    if field[x][y] == " ":
                        return x, y
                    else:
                        print("Клетка занята.")
                else:
                    print("Координаты за пределами игрового поля.")
            else:
                print("Координаты должны вводится числами.")


def game():
    start_game()
    count = 0
    while True:
        count += 1
        playground()

        if count % 2 == 1:
            print("Ходит крестик.")
        else:
            print("Ходит нолик.")

        x, y = req_coordinates()

        if count % 2 == 1:
            field[x][y] = 'X'
        else:
            field[x][y] = '0'

        if end_game(count):
            print("---------------")
            print("Игра окончена.")
            break


def end_game(count):
    w_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
              ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
              ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    if count == 9:
        print("---------------")
        print("Ничья.")
        return True
    else:
        for comb in w_comb:
            symbols = []
            for i in comb:
                symbols.append(field[i[0]][i[1]])
            if symbols == ["X", "X", "X"]:
                print("---------------")
                print("Выиграли крестики")
                return True
            if symbols == ["0", "0", "0"]:
                print("---------------")
                print("Выиграли нолики")
                return True
        return False


game()



