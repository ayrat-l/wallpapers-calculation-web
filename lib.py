import math

def wallpapers_calc(width_room,lenght_room,height_room,width_wallpapers,lenght_wallpapers):
    stock = 0.10 # Запасные 10 см к длине обоев
    """
    >>> wallpapers_calc(3,6,2.6,1.4,10)
    4

    """
    #Периметр комнаты
    perimeter_room = (width_room + lenght_room) * 2

    #Узнаем количество полотнищ
    count_canvas = math.ceil(perimeter_room / width_wallpapers)

    #Из одного рулона выйдет __ полотна
    count_canvas_in_1_wallpapers = math.floor(lenght_wallpapers / (height_room + stock))

    #Обоев всего понадобится
    wallpapers_calc = count_wallpapers = math.floor(count_canvas /count_canvas_in_1_wallpapers)
    return wallpapers_calc



