import pytest
import allure
from http import HTTPStatus
from data.courier_generator import CourierGenerator
from helpers.courier_helper import CourierHelper
from message import INSUFFICIENT_DATA_MESSAGE, LOGIN_ALREADY_EXISTS_MESSAGE


@allure.feature('Создание курьера')
@allure.description('Тесты создания курьера: успешное создание, дубликаты, проверка обязательных полей и поведение при существующем логине.')
class TestCourierCreation:

    @allure.title('Курьера можно создать')
    @allure.description('Успешное создание курьера возвращает 201 и {"ok": true}.')
    def test_create_courier_success(self, courier_creds):
        response = CourierHelper.create_courier(courier_creds)

        assert response.status_code == HTTPStatus.CREATED
        assert response.json()['ok'] is True
        
        """Фикстура для удаления курьера после теста"""
        CourierHelper.delete_courier(courier_creds) 

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description('Попытка создать курьера с уже существующими данными возвращает ошибку конфликта.')
    def test_create_duplicate_courier(self, courier):
        response = CourierHelper.create_courier(courier)

        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json().get('message') == LOGIN_ALREADY_EXISTS_MESSAGE

    @allure.title('Для создания нужны все обязательные поля')
    @allure.description('Если отсутствует login или password — возвращается 400 и сообщение о недостаточности данных.')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_required_field(self, courier_creds, missing_field):
        courier_data = dict(courier_creds)
        courier_data.pop(missing_field, None)
        response = CourierHelper.create_courier(courier_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json().get('message') == INSUFFICIENT_DATA_MESSAGE

    @allure.title('Если логин уже существует — возвращается ошибка')
    @allure.description('Попытка создать курьера с логином, который уже используется, возвращает сообщение об ошибке.')
    def test_create_courier_existing_login(self, courier):
        new_courier = CourierGenerator.random_courier()
        new_courier['login'] = courier['login']

        response = CourierHelper.create_courier(new_courier)
        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json().get('message') == LOGIN_ALREADY_EXISTS_MESSAGE