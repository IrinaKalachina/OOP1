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