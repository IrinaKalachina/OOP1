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

    def add_vehicle(self, vehicle):
        """Добавление транспорта в класс"""
        self.__vehicles.append(vehicle)

    def add_driver(self, driver):
        """Добавление водителя в класс"""
        self.__drivers.append(driver)

    def __str__(self):
        """Метод перевода объекта в строку"""
        return self.__name
class Vehicle:
    """Класс транспорт"""
    def __init__(self, tip, count):
        self._tip = tip  # Тип авто
        self._count = count  # Количество единиц
    def tip(self):
        return self._tip

    def __str__(self):
        return f"{self._tip} {self._count}"

class Driver:
    """Класс водитель"""
    def __init__(self, name, age):
        self._name = name  # Имя
        self._age = age  # Возраст

    def __str__(self):
        return f"{self._name} {self._age}"

def create_company():
    """Создание фирмы"""
    name = input("Введите название фирмы: ")
    if not isinstance(name, str):
        print("Название указано неверно!")
    else:
        return Company(name)

def create_vehicle():
    """Создание транспорта"""
    tip = input("Введите тип транспорта: ")
    if not tip.isdigit():
        try:
            count = int(input("Введите количество единиц транспорта: "))  # Преобразуем введенное значение в целое число
            return Vehicle(tip, count)
        except ValueError:
            print("Ошибка: Количество транспорта должно быть целым числом.")
    else: print("Тип указан неверно!")

def create_driver():
    """Создание водителя"""
    name = input("Введите имя водителя: ")
    if not name.isdigit():
        try:
            age = int(input("Введите возраст водителя: "))  # Преобразуем введенное значение в целое число
            return Driver(name, age)
        except ValueError:
            print("Ошибка: Возраст водителя должен быть целым числом.")
    else: print("Имя указано неверно!")
def main():
    companies = []
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

        if choice == "1":
            company = create_company()
            if company is not None:
                companies.append(company)
                print(f"Фирма '{company}' создана.")
        elif choice == "2":
            if not companies:
                print("Сначала создайте фирму.")
                continue
            company_index = int(input("Введите номер фирмы для добавления транспорта: ")) - 1
            if 0 <= company_index < len(companies):
                vehicle = create_vehicle()
                if vehicle is not None:
                    companies[company_index].add_vehicle(vehicle)
                    print(f"Транспорт '{vehicle}' добавлен к фирме '{companies[company_index]}'.")
                else:
                    print("Транспорт не был создан.")
            else:
                print("Неправильный номер фирмы.")
        elif choice == "3":
            if not companies:
                print("Сначала создайте фирму.")
                continue
            company_index = int(input("Введите номер фирмы для добавления водителя: ")) - 1
            if 0 <= company_index < len(companies):
                driver = create_driver()
                if driver is not None:
                    companies[company_index].add_driver(driver)
                    print(f"Водитель '{driver}' добавлен к фирме '{companies[company_index]}'.")
                else:
                    print("Водитель не был создан.")
            else:
                print("Неправильный номер фирмы.")
        elif choice == "4":
            print("\nСписок фирм:")
            for i, company in enumerate(companies, start=1):
                print(f"{i}. {company}")
        elif choice == "5":
            print("\nСписок транспорта:")
            for i, company in enumerate(companies, start=1):
                print(f"Транспорт у фирмы '{company}':")
                for j, vehicle in enumerate(company.vehicles, start=1):
                    print(f'{j}. {vehicle} единиц')
        elif choice == "6":
            print("\nСписок водителей:")
            for company in companies:
                print(f"Водители у фирмы '{company}':")
                for driver in company.drivers:
                    print(driver, ' лет')
        elif choice == "7":
            if not companies:
                print("Нет доступных фирм.")
                continue
            company_index = int(input("Введите номер фирмы для просмотра (по порядку): ")) - 1
            if 0 <= company_index < len(companies):
                print(f"Фирма: {companies[company_index]}")
                print("Транспорт:")
                for vehicle in companies[company_index].vehicles:
                    print(f"- {vehicle}")
                print("Водители:")
                for driver in companies[company_index].drivers:
                    print(f'- {driver} лет')
            else:
                print("Неправильный номер фирмы.")
        elif choice == "8":
            print("Программа завершена.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()