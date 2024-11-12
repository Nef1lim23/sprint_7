import requests
from data import *
import allure


class CourierMethods:
    @allure.step('Создание курьера')
    def post_create_couriers(self, payload):
        r = requests.post(f'{URLs.BASE_URL}{URLs.CREATE_COURIER_URL}', data=payload)
        return r

    @allure.step('Создание одинаковых курьеров')
    def post_create_couriers_identical(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1],
            'firstName': login_pass[2]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.CREATE_COURIER_URL}', data=payload)
        return response

    @allure.step('Получение ID курьера')
    def get_id_courier(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        log_in_response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return log_in_response.json()['id']

    @allure.step('Удаление созданого курьерчика')
    def delete_created_courier(self, login_pass):
        courier_id = self.get_id_courier(login_pass)
        requests.delete(f'{URLs.BASE_URL}{URLs.DELETE_COURIER_URL}{courier_id}')

    @allure.step('Авторизация курьера')
    def post_login_courier(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', json=payload)
        return response

    @allure.step('Авторизация курьера без пароля')
    def post_login_courier_without_password(self, login_pass):
        payload = {
            'login': login_pass[0],
            'password': ''
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return response

    @allure.step('Авторизация курьера без логина')
    def post_login_courier_without_login(self, login_pass):
        payload = {
            'login': '',
            'password': login_pass[1]
        }
        response = requests.post(f'{URLs.BASE_URL}{URLs.LOGIN_COURIER_URL}', data=payload)
        return response

  #  @allure.step