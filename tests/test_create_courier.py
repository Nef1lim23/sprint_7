import allure
import pytest
import requests
from data import *

from methods.courier_methods import CourierMethods


class TestCouriersEndpoints:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Проверяем код ответа и тело')
    def test_create_courier_success(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, r = create_courier
        assert r.status_code == 201 and r.json() == {'ok': True}
        courier_methods.delete_created_courier(login_pass)

    @allure.title('Проверка,что нельзя создать двух одинаковых курьеров')
    @allure.description('попытка создать дубль курьера, так же проверка кода ответа и сообщения')
    def test_create_courier_duplicate(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_create_couriers_identical(login_pass)
        assert r.json()['code'] == 409 and Errors.error_create_409_already_exist in r.json()['message']
        courier_methods.post_create_couriers_identical(login_pass)
        courier_methods.delete_created_courier(login_pass)

    @allure.title('Проверка создания курьера без обязательного поля')
    @allure.description('Создаем курьера убирая одно обязательное поле ')
    @pytest.mark.parametrize('payload', InvalidDataForRegistration.payloads)
    def test_create_courier_missing_field(self, payload):
        courier_methods = CourierMethods()
        r = courier_methods.post_create_couriers(payload)
        assert r.json()['code'] == 400 and Errors.error_create_400_no_data in r.json()['message']
