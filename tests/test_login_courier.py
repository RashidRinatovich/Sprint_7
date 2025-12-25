import pytest
import allure
from http import HTTPStatus
from helpers.courier_helper import CourierHelper
from data.courier_generator import CourierGenerator
from message import ACCOUNT_NOT_FOUND_MESSAGE, INSUFFICIENT_LOGIN_DATA_MESSAGE
from data.test_data import WRONG_PASSWORD, WRONG_LOGIN


@allure.feature('Авторизация курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    @allure.description('Успешная авторизация с валидными учетными данными возвращает id')
    def test_courier_can_login(self, created_courier):
        """Курьер может авторизоваться"""
        with allure.step('Подготовить валидные учетные данные'):
            credentials = {
                'login': created_courier['login'],
                'password': created_courier['password']
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить успешный ответ и наличие id'):
            assert response.status_code == HTTPStatus.OK
            assert 'id' in response.json()
            assert isinstance(response.json()['id'], int)

    @allure.title('Успешный запрос возвращает id')
    @allure.description('Проверка, что в теле успешного ответа присутствует поле id')
    def test_login_returns_courier_id(self, created_courier):
        """Успешный запрос возвращает id"""
        with allure.step('Подготовить валидные учетные данные'):
            credentials = {
                'login': created_courier['login'],
                'password': created_courier['password']
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить наличие id в ответе'):
            assert response.status_code == HTTPStatus.OK
            response_data = response.json()
            assert 'id' in response_data
            assert response_data['id'] is not None

    @allure.title('Для авторизации нужны все обязательные поля')
    @allure.description('Если отсутствует login или password — статус 400 и корректное сообщение')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    
    def test_login_missing_required_field(self, created_courier, missing_field):
        """Если какого-то поля нет, запрос возвращает ошибку"""
        with allure.step(f'Подготовить данные без поля {missing_field}'):
            credentials = {
                'login': created_courier['login'],
                'password': created_courier['password']
            }
            credentials.pop(missing_field, None)

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить статус 400 и сообщение об ошибке'):
            assert response.status_code == HTTPStatus.BAD_REQUEST
            assert response.json().get('message') == INSUFFICIENT_LOGIN_DATA_MESSAGE

    @allure.title('Ошибка при неверном пароле')
    @allure.description('Неверный пароль приводит к статусу 404 и сообщению о ненайденном аккаунте')
    def test_login_with_wrong_password(self, created_courier):
        """Система вернёт ошибку, если неправильно указать пароль"""
        with allure.step('Подготовить данные с неверным паролем'):
            credentials = {
                'login': created_courier['login'],
                'password': WRONG_PASSWORD
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить статус 404 и текст ошибки'):
            assert response.status_code == HTTPStatus.NOT_FOUND
            assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE

    @allure.title('Ошибка при неверном логине')
    @allure.description('Неверный логин приводит к статусу 404 и сообщению о ненайденном аккаунте')
    def test_login_with_wrong_login(self, created_courier):
        """Система вернёт ошибку, если неправильно указать логин"""
        with allure.step('Подготовить данные с неверным логином'):
            credentials = {
                'login': WRONG_LOGIN,
                'password': created_courier['password']
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить статус 404 и текст ошибки'):
            assert response.status_code == HTTPStatus.NOT_FOUND
            assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE

    @allure.title('Ошибка для несуществующего пользователя')
    @allure.description('Авторизация несуществующего аккаунта возвращает 404 и корректное сообщение')
    def test_login_nonexistent_user(self):
        """Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку"""
        with allure.step('Сгенерировать данные несуществующего курьера'):
            fake_courier = CourierGenerator.random_courier()
            credentials = {
                'login': fake_courier['login'],
                'password': fake_courier['password']
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierHelper.login_courier(credentials)

        with allure.step('Проверить статус 404 и текст ошибки'):
            assert response.status_code == HTTPStatus.NOT_FOUND
            assert response.json().get('message') == ACCOUNT_NOT_FOUND_MESSAGE