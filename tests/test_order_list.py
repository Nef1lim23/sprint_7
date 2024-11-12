import allure
import pytest
import requests
from data import *

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


class TestOrderList:
    @allure.title('Проверка ,что в тело ответа возвращается список заказов')
    @allure.description('Проверка кода и тела ответа')
    def test_get_list_order(self):
        order_list = OrderMethods()
        response = order_list.get_list_orders()
        assert type(response.json()['orders']) == list and 'id' in response.json()['orders'][0]
