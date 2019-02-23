from lib import wallpapers_calc

width_room = float(input("Введите ширину комнаты > "))
lenght_room = float(input("Введите длину комнаты > "))
height_room = float(input("Введите высоту комнаты > "))

width_wallpapers = float(input("Введите ширину рулона обоев > "))
lenght_wallpapers = float(input("Введите длину рулона обоев > "))

print("Необходимо купить рулонов обоев в количестве", wallpapers_calc(width_room,lenght_room,height_room,width_wallpapers,lenght_wallpapers), "штук.")