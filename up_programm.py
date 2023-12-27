# Создаем базу данных машин
available_cars = {
    'Toyota': {
        'Corolla': 15000,
        'Camry': 25000,
        'Rav4': 30000
    },
    'Honda': {
        'Civic': 17000,
        'Accord': 26000,
        'CR-V': 32000
    },
    'Ford': {
        'Fiesta': 14000,
        'Focus': 20000,
        'Mustang': 35000
    }
    # Можно добавить другие марки и их модели с ценами
}
def select_car_brand():
    print("Для выбора марки машины нажмите '1'")
    print("Для выхода из программы нажмите '2'")

    while True:
        user_choice = input("Введите ваш выбор: ")

        if user_choice == '1':
            print("Доступные марки машин в нашей компании:")
            for brand in available_cars.keys():
                print(brand)

            while True:
                user_brand = input("Введите марку машины: ")
                if user_brand in available_cars:
                    return user_brand
                else:
                    print("Извините, такой марки машины у нас нет. Пожалуйста, выберите из списка доступных марок.")

        elif user_choice == '2':
            print("Выход из программы.")
            exit()

        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию '1' или '2'.")

def browse_car_models(brand):
    print(f"Доступные модели машин марки {brand}:")
    for model, price in available_cars[brand].items():
        print(f"{model}: {price}")

    while True:
        user_budget = float(input("Введите сумму вашего бюджета: "))

        affordable_models = {model: price for model, price in available_cars[brand].items() if price <= user_budget}

        if affordable_models:
            print("Модели машин, подходящие по стоимости:")
            for model, price in affordable_models.items():
                print(f"{model}: {price}")

            while True:
                user_choice = input("Для выбора модели введите '1', для возврата к выбору марки введите '2': ")

                if user_choice == '1':
                    return
                elif user_choice == '2':
                    return select_car_brand()
                else:
                    print("Некорректный ввод. Пожалуйста, выберите опцию '1' или '2'.")
        else:
            print("К сожалению, у нас нет моделей машин данной марки в пределах вашего бюджета.")
            return select_car_brand()

# Пример использования функции
selected_brand = select_car_brand()
print(f"Вы выбрали марку машины: {selected_brand}")
browse_car_models(selected_brand)
