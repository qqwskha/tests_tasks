from src.geometry import Circle, Triangle, calculate_area

def get_positive_float(prompt):
    """Получает положительное число от пользователя."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Значение должно быть положительным числом. Попробуйте снова.")
            else:
                return value
        except ValueError:
            print("Некорректный ввод. Введите число.")

def get_triangle_sides():
    """Получает три стороны треугольника от пользователя."""
    print("Введите стороны треугольника:")
    a = get_positive_float("Сторона a: ")
    b = get_positive_float("Сторона b: ")
    c = get_positive_float("Сторона c: ")

    # Проверяем, могут ли стороны образовать треугольник
    if a + b <= c or a + c <= b or b + c <= a:
        print("Такого треугольника не существует! Попробуйте снова.")
        return get_triangle_sides()  # Рекурсивно просим ввести снова
    return a, b, c

def main():
    print("Добро пожаловать в программу для вычисления площадей фигур!")
    print("Выберите фигуру:")
    print("1. Круг")
    print("2. Треугольник")

    choice = input("Введите номер фигуры (1 или 2): ").strip()

    if choice == "1":
        # Вычисление площади круга
        radius = get_positive_float("Введите радиус круга: ")
        try:
            circle = Circle(radius)
            print(f"Площадь круга с радиусом {radius}: {circle.area():.2f}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "2":
        # Вычисление площади треугольника
        a, b, c = get_triangle_sides()
        try:
            triangle = Triangle(a, b, c)
            print(f"Площадь треугольника со сторонами {a}, {b}, {c}: {triangle.area():.2f}")
            if triangle.is_right_triangle():
                print("Этот треугольник прямоугольный!")
            else:
                print("Этот треугольник НЕ прямоугольный.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    else:
        print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()