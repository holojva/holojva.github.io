def build_roof(r, rc) :
    """
    input: r - data for build roof, rc - data for roof color
    return: bool
    """
    pass
def build_walls(r, wc) :
    """
    input: r - data for build walls, wc - data for walls color
    return: bool
    """
    pass
def build_door(r, dc) :
    """
    input: r - data for build door, dc - data for door color
    return: bool
    """
    pass
def build_house(my_dream, colors) :
    house = False
    roof_color = color[0]
    house_color = color[1]
    door_color = color[2]
    roof = my_dream[0]
    walls = my_dream[1]
    while not house:
        roof_status = build_roof(roof, roof_color)
        walls_status = build_walls(walls, house_color)
        door_status = build_door(door_color, door_color)
        if roof_status == True walls_status == True door_status == True :
            house = True
            print("Поздравляю, вы построили дом мечты!")
idea = ("roof", "walls")
color = ("red", "white", "blue")
build_house(idea, color)
