def square(side):
    area = side * side
    return int(area) if area == int(area) else int(area) + 1


side = float(input("Введите сторону квадрата: "))

print(square(side))
