import requests
import allure
from urls import CourierUrls


class CourierHelper:

    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(courier_data):
        with allure.step('POST /api/v1/courier'):
            return requests.post(CourierUrls.CREATE_COURIER, json=courier_data)

    @staticmethod
    @allure.step('Авторизация курьера')
    def login_courier(credentials):
        with allure.step('POST /api/v1/courier/login'):
            return requests.post(CourierUrls.LOGIN_COURIER, json=credentials)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(courier_data):
        with allure.step('Логин курьера для получения id'):
            login_response = CourierHelper.login_courier({
                'login': courier_data['login'],
                'password': courier_data['password']
            })

        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            with allure.step(f'DELETE /api/v1/courier/{{id}} (id={courier_id})'):
                return requests.delete(CourierUrls.DELETE_COURIER.format(courier_id=courier_id))