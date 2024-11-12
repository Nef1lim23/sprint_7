import requests
from data import *
import allure
import json


class OrderMethods:
    @allure.step("Создать заказ")
    def post_orders(self, order_data):
        order_data = json.dumps(order_data)
        headers = {'Content-Type': 'application/json'}
        r = requests.post(f'{URLs.BASE_URL}{URLs.CREATE_ORDERS_URL}', data=order_data, headers=headers)
        return r

    @allure.step("Получение списка заказов")
    def get_list_orders(self):
        r = requests.get(f'{URLs.BASE_URL}{URLs.CREATE_ORDERS_URL}')
        return r
