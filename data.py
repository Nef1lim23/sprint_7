class URLs:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDERS_URL = '/api/v1/orders'
    CREATE_COURIER_URL = '/api/v1/courier'
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    DELETE_COURIER_URL = '/api/v1/courier/'
    CREATE_ORDERS_URL = '/api/v1/orders'
    GET_ORDERS_URL = '/api/v1/orders'


class Errors:
    error_login_400_no_login_or_pass = "Недостаточно данных для входа"
    error_login_404_no_such_user = "Учетная запись не найдена"
    error_create_400_no_data = "Недостаточно данных для создания учетной записи"
    error_create_409_already_exist = "Этот логин уже используется."
    error_delete_400_no_data = "Недостаточно данных для удаления курьера"
    error_delete_404_no_such_id = "Курьера с таким id нет."
    error_count_orders_no_data = "Недостаточно данных для поиска"
    error_count_orders_no_such_user = "Курьер не найден"
    error_track_order_no_data = "Недостаточно данных для поиска"
    error_track_order_no_such_order = "Заказ не найден"
    error_accept_order_no_order_number = "Недостаточно данных для поиска"
    error_accept_order_no_such_courier = "Курьера с таким id не существует"
    error_accept_order_no_data = "Недостаточно данных для поиска"


class InvalidDataForRegistration:
    payloads = [
        {
            'login': '1337zone@mail.ru',
            'password': '',
            'first_name': 'Sergey',
        },
        {
            'login': '',
            'password': 'samuraiRIck',
            'first_name': 'Rick',
        }
    ]


class InvalidDataForLogin:
    payloads = [['1337zone@mail.ru', 'fgfgdfg'], ['yabpgoergi', 'samuraiRIck']]


class OrderData:
    order_data_black = {
        "firstName": "Amidamaru",
        "lastName": "Shamankingovivch",
        "address": "Japan",
        "metroStation": 3,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-11-28",
        "comment": "Amidamaru to the sword",
        "color": [
            "BLACK"
        ]}

    order_data_grey = {
        "firstName": "Amidamaru",
        "lastName": "Shamankingovivch",
        "address": "Japan",
        "metroStation": 3,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-11-28",
        "comment": "Amidamaru to the sword",
        "color": [
            "GREY"
        ]
    }

    order_data_grey_black = {
        "firstName": "Amidamaru",
        "lastName": "Shamankingovivch",
        "address": "Japan",
        "metroStation": 3,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-11-28",
        "comment": "Amidamaru to the sword",
        "color": [
            "BLACK", "GREY"
        ]
    }

    order_data_without_color = {
        "firstName": "Amidamaru",
        "lastName": "Shamankingovivch",
        "address": "Japan",
        "metroStation": 3,
        "phone": "+7 800 555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-11-28",
        "comment": "Amidamaru to the sword",
        "color": []
    }
