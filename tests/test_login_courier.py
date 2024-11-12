import allure
from methods.courier_methods import CourierMethods
from data import *
import pytest


class TestLoginCourier:
    @allure.title('Проверка курьер может авторизоваться')
    @allure.description('Проверяем код ответа и тело')
    def test_authorization_courier(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier(login_pass)
        assert r.status_code == 200 and r.json()['id'] == courier_methods.get_id_courier(login_pass)
        courier_methods.delete_created_courier(login_pass)


    @allure.title('Проверка получения ошибки аутентификации курьера при вводе несуществующей пары логина и пароля')
    @allure.description('Передаем данные без логина или пароля.''Проверяются код и тело ответа.')
    @pytest.mark.parametrize('payload', InvalidDataForLogin.payloads)
    def test_create_courier_incorrect_data(self, payload):
        courier_methods = CourierMethods()
        r = courier_methods.post_login_courier(payload)
        assert r.status_code == 404 and Errors.error_login_404_no_such_user in r.json()['message']

    @allure.title('Проверка получения ошибки при авторизации курьера без логина')
    @allure.description('Передаем данные без логина. Проверка кода и тела ответа.')
    def test_create_courier_missing_login(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier_without_login(login_pass)
        assert r.status_code == 400 and Errors.error_login_400_no_login_or_pass == r.json()['message']

    @allure.title('Проверка получения ошибки при авторизации курьера без пароля')
    @allure.description('Передаем данные без пароля. Проверка кода и тела ответа.')
    def test_create_courier_missing_password(self, create_courier):
        courier_methods = CourierMethods()
        login_pass, _ = create_courier
        r = courier_methods.post_login_courier_without_password(login_pass)
        assert r.status_code == 400 and Errors.error_login_400_no_login_or_pass == r.json()['message']
