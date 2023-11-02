class Company:
    """Описание фирмы"""

    def __init__(self, __name):  # Присвоение атрибутам значений
        self.__name = __name  # Атрибуты
        self.__vehicles = []  # транспорт
        self.__drivers = []  # водители

    """Методы"""

    @property
    def vehicles(self):
        return self.__vehicles

    @property
    def drivers(self):
        return self.__drivers

    def add_vehicle(self, vehicle):  # Добавление транспорта в класс
        self.__vehicles.append(vehicle)

    def add_driver(self, driver):  # Добавление водителя в класс
        self.__drivers.append(driver)

    def __str__(self):  # Метод перевода объекта в строку
        return self.__name
class Vehicle:  # Класс транспорт
    def __init__(self, tip, count):
        self._tip = tip  # Тип авто
        self._count = count  # Количество единиц

    def tip(self):
        return self._tip

    def __str__(self):
        return f"{self._tip} {self._count}"

class Driver:  # Класс водитель
    def __init__(self, name, age):
        self._name = name  # Имя
        self._age = age  # Возраст

    def __str__(self):
        return f"{self._name} {self._age}"

def create_company():  # Создание фирмы
    name = input("Введите название фирмы: ")
    if not isinstance(name, str):
        print("Название указано неверно!")
    else:
        return Company(name)

def create_vehicle():  # Создание транспорта
    tip = input("Введите тип транспорта: ")
    if not tip.isdigit():
        try:
            count = int(input("Введите количество единиц транспорта: "))  # Преобразуем введенное значение в целое число
            return Vehicle(tip, count)
        except ValueError:
            print("Ошибка: Количество транспорта должно быть целым числом.")
    else: print("Тип указан неверно!")

def main():
    while True:
        print("\nМеню:")
        print("1. Создать новую фирму\n"
              "2. Создать новый транспорт\n"
              "3. Создать нового водителя\n"
              "4. Вывести содержимое фирм\n"
              "5. Вывести содержимое транспорта\n"
              "6. Вывести содержимое водителей\n"
              "7. Вывести представление конкретной фирмы\n"
              "8. Завершить работу программы")

        choice = input("Выберите действие: ")


if __name__ == "__main__":
    main()