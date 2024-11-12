import pytest
import requests
from data import *
import allure

from methods.order_methods import OrderMethods


class TestOrderCreate:
    @allure.title('проверка создания заказа с указанием разного цвета')
    @allure.description('Проверка создания заказа с указанием цвета')
    @pytest.mark.parametrize('order_data', [OrderData.order_data_black,
                                            OrderData.order_data_grey,
                                            OrderData.order_data_grey_black,
                                            OrderData.order_data_without_color])
    def test_create_order_with_different_color(self, order_data):
        create_order = OrderMethods()
        r = create_order.post_orders(order_data)
        assert r.status_code == 201 and 'track' in r.text

