import math


# Функция для расчёта расстояния между двумя точками
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Функция для нахождения кратчайшего пути
def find_shortest_path(points):
    path = [points[0]]  # Начинаем с первой точки
    remaining_points = points[1:]  # Остальные точки

    while remaining_points:
        # Ищем ближайшую точку к текущей
        current_point = path[-1]
        next_point = min(remaining_points, key=lambda point: calculate_distance(current_point, point))
        path.append(next_point)
        remaining_points.remove(next_point)

    return path


# Пример использования
coordinates = [(-1821, 704), (-3000, -1005), (1004, 104), (10000, -900)]
shortest_path = find_shortest_path(coordinates)

print("Кратчайший маршрут:")
for point in shortest_path:
    print(point)
