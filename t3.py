#завдання 3. магічні методи та перевантаження операторів

class Vector:
    def __init__(self, *components):
        #зберігаємо координати вектора як кортеж
        self.components = tuple(components)

    #категорія 1: представлення
    def __str__(self):
        # для користувача (людиночитне)
        return f"вектор{self.components}"

    def __repr__(self):
        #для розробника (однозначне)
        return f"Vector{self.components}"

    #kатегорія 2: арифметика
    def __add__(self, other):
        #додавання векторів повертає новий екземпляр
        if len(self) != len(other):
            raise ValueError("вектори повинні мати однакову довжину")
        new_coords = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*new_coords)

    def __sub__(self, other):
        #віднімання векторів
        if len(self) != len(other):
            raise ValueError("вектори повинні мати однакову довжину")
        new_coords = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*new_coords)

    #категорія 3: порівняння
    def __eq__(self, other):
        # перевірка на рівність
        if not isinstance(other, Vector):
            return False
        return self.components == other.components

    #категорія 4: контейнер/виклик
    def __len__(self):
        # виклик функції len() - повертає розмірність вектора (кількість координат)
        return len(self.components)

    def __abs__(self):
        #виклик функції abs() - повертає довжину вектора (модуль)
        #обчислюється як корінь із суми квадратів координат
        length_sq = sum(x ** 2 for x in self.components)
        return length_sq ** 0.5


def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(1, 2, 3)

    print("демонстрація магічних методів:")

    #виклик методів через стандартні оператори та функції
    print(f"str(v1): {str(v1)}")
    print(f"repr(v1): {repr(v1)}")

    v_sum = v1 + v2
    print(f"додавання (v1 + v2): {v_sum}")

    v_sub = v2 - v1
    print(f"віднімання (v2 - v1): {v_sub}")

    print(f"порівняння (v1 == v3): {v1 == v3}")
    print(f"порівняння (v1 == v2): {v1 == v2}")

    print(f"розмірність вектора (len(v1)): {len(v1)}")
    print(f"довжина вектора (abs(v1)): {abs(v1)}")


if __name__ == "__main__":
    main()