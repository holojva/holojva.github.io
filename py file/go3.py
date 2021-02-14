import pickle
import os
def saver(save) :
    file_of_save = input("Напишите название файла сохранения на английском: ")
    with open(f"save/{file_of_save}.dat", "wb") as sf :
        pickle.dump(save, sf)
    print("Сохранение создано!")
def loader(path) :
    name_of_save = input("Напишите название файла сохранения. Если ошибетесь, игра сломается! ")
    if name_of_save + '.dat' in os.listdir('save'): 
        with open(f"save/{name_of_save}.dat", "rb") as lf :
            load_data = pickle.load(lf)
        return load_data
    else: 
        print('VVEDI NORMALNOE NAZVANIE!!!!!!')
        loader(path)
    with open(f"save/{name_of_save}.dat", "rb") as lf :
        load_data = pickle.load(lf)
    return load_data
def can_i_go(x, y, boom) :
    """
    input: x and y coordinates, boom - list of coorinates of obstacles
    output: False if in boom finded array with x and y, else True 
    """
    for i in boom :
        if i[0] == x :
            if i[1] == y :
                return False
    return True
def create_field(hm) :
    """
        input: hm - size of the field
        output: arr - lists with printing information, obstacles - coordinates of obstacles
    """
    import random
    arr = []
    obstacles = []
    for j in range(hm) :
        arr += [[]]
        for i in range(hm) :
            if bool(random.randint(0, 3)) :
                k = "1"
            else : 
                k = "0"
                obstacles += [[i, j]]
            arr[j] += [k]
    return [arr, obstacles]

def drawing_field(for_print) :
    """
    input: for_print - array with info to print
    output: None, used it just how print the field function
    """ 
    for i in for_print :
        print("".join(i))
        
        # if y == i :
        #     for j in range(hm) :
        #         if x == j :
                    
        #             print()
        # else :
        #     print(str(field * hm))
def move_person(x, y, to, hm, bombs, save, path) :
    """
    input: x - x coordinate of item, y - y coordinate of item, to - int, 0 if left, 1 if right, 2 if down, 3 if up, else 4, 
    hm - size of the field, bombs - coordinates of obstacles, for_print - what we want to print.
    output: new x and y coordinates
    """
    if to == 0 :  
        x -= 1
        if not can_i_go(x, y, bombs) :
            print("Это препятствие") 
            x += 1
        elif x == -1:
            x += hm
            if not can_i_go(x, y, bombs) :
                print("Это препятствие") 
                x -= hm
    elif to == 1 :
        x += 1
        if not can_i_go(x, y, bombs) :
            print("Это препятствие") 
            x -= 1
        elif x == hm :
            x -= hm
            if not can_i_go(x, y, bombs) :
                print("Это препятствие") 
                x += hm
    elif to == 2 or to == 6 :
        y += 1
        if not can_i_go(x, y, bombs) :
            print("Это препятствие") 
            y -= 1
        elif y == hm :
            y -= hm
            if not can_i_go(x, y, bombs) :
                print("Это препятствие") 
                y += hm
    elif to == 3 :
        y -= 1
        if not can_i_go(x, y, bombs) :
            print("Это препятствие") 
            y += 1
        elif y == -1:
            y += hm
            if not can_i_go(x, y, bombs) :
                print("Это препятствие") 
                y -= hm
    elif to == 4 :
        return loader(path)
    elif to == 5 :
        saver(save)
    return [x, y]
def to_the() :
    
    """
    output: 0 if left, 1 if right, 2 if down, 3 if up, 4 if load, 5 if save, else 6.
    """
    to = input("Куда вы хотите пойти? Варианты ответов: загрузить игру - load, сохранить игру - save, налево - a, направо - d, вниз - s, вверх - w. Если ошибетесь, автоматически пойдете вниз ")
    if to == "a" : 
        return 0
    elif to == "d" : 
        return 1
    elif to == "s" : 
        return 2
    elif to == "w" : 
        return 3
    elif to == "load" : 
        return 4
    elif to == "save" : 
        return 5
    else :
        return 6
def game() :
    x = 0
    y = 0
    size = int(input("Какого размера будет поле? "))
    progress = True
    j = create_field(size)
    for_print = j[0]
    bombs = j[1]
    for_print[y][x] = "X"
    to = 0
    if not os.path.isdir('./save') :
        path = os.getcwd()
        os.mkdir(path + "/save")
    # print(for_print)
    # print(bombs)
    while progress :
        save = [x, y, size, progress, j, for_print, bombs, to]
        to = to_the()
        i = move_person(x, y, to, size, bombs, save, path)
        if len(i) == len(save) :
            size = i[2]
            progress = i[3]
            j = i[4]
            for_print = i[5]
            bombs = i[6]
            to = i[7]
            i = [i[0], i[1]]
        for_print[y][x] = "-"
        x = i[0]
        y = i[1]
        for_print[y][x] = "X"
        drawing_field(for_print)
game()
