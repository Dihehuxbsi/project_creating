from concurrent.futures import ThreadPoolExecutor
# База данных машин
cars = {
    "Toyota": {
        "Corolla": 10000,
        "Camry": 15000,
        "RAV4": 20000
    },
    "Honda": {
        "Civic": 12000,
        "Accord": 18000,
        "CR-V": 22000
    },
    "Nissan": {
        "Sentra": 11000,
        "Altima": 17000,
        "Rogue": 21000
    },
    "Ford": {
        "Focus": 9000,
        "Fusion": 13000,
        "Escape": 17000
    },
    "Chevrolet": {
        "Cruze": 11000,
        "Malibu": 16000,
        "Equinox": 21000
    }
}

# Вывод списка марок машин
car_brands = list(cars.keys())
print("Доступные марки машин: ", car_brands)

while True:
    # Получение марки машины от пользователя
    car_brand = input("Введите марку машины: ")

    # Проверка наличия марки в базе данных
    if car_brand not in car_brands:
        print("К сожалению, такой марки машины нет в нашей базе данных. Попробуйте еще раз.")
        continue

    # Получение бюджета от пользователя
    budget = int(input("Введите ваш бюджет: "))

    # Получение моделей и цен на машины данной марки в пределах бюджета
    car_models = cars[car_brand]
    available_models = {model: price for model, price in car_models.items() if price <= budget}

    # Функция для вывода доступных моделей и цен на машины
    def print_available_models(models):
        print("Доступные модели и цены:")
        for model, price in models.items():
            print(f"{model} - {price}")

    # Вывод доступных моделей и цен на них в отдельном потоке
    with ThreadPoolExecutor() as executor:
        executor.submit(print_available_models, available_models)
        # Вывод доступных моделей и цен на них
    while True:
        print("Доступные модели и цены:")
        for model, price in available_models.items():
            print(f"{model} - {price}")

        # Добавляем опцию "Другой выбор"
        print("Другой выбор")

        # Получение выбора пользователя
        car_model = input("Введите модель машины: ")

        # Если выбрана опция "Другой выбор", то выходим из цикла и начинаем заново
        if car_model == "Другой выбор":
            break

        # Проверка наличия выбранной модели в базе данных
        if car_model not in available_models:
            print("К сожалению, такой модели машины нет в нашей базе данных. Попробуйте еще раз.")
            continue

        # Вывод приятного сообщения с информацией о выбранной машине
        print(
            "Отличный выбор! Вы выбрали car_brand {car_model} за {available_models[car_model]} долларов. Поздравляем вас с покупкой! Наслаждайтесь ездой.")
        break

    # Вопрос пользователю о продолжении работы с базой данных
    answer = input("Хотите продолжить работу с базой данных? (да/нет) ")
    if answer.lower() == "нет":
        break

print("Работа с базой данных завершена.")