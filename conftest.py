import pytest
import allure
from helpers.courier_helper import CourierHelper
from helpers.order_helper import OrderHelper
from data.courier_generator import CourierGenerator
from data.order_generator import OrderGenerator
from data.order_test_data import STATUS_CREATED, FIELD_TRACK


@pytest.fixture
def courier():
    """Фикстура для создания тестового курьера"""
    with allure.step('Генерировать данные курьера'):
        courier_data = CourierGenerator.random_courier()
    with allure.step('Создать курьера'):
        response = CourierHelper.create_courier(courier_data)

@pytest.fixture()
def delete_courier_after_test(courier_creds):
     """Фикстура для удаления курьера после теста"""
     yield courier_creds                             
     CourierHelper.delete_courier(courier_creds)  


@pytest.fixture
def courier_creds():
    """Фикстура для получения учетных данных курьера"""
    with allure.step('Сгенерировать учетные данные курьера'):
        courier_data = CourierGenerator.random_courier()
        credentials = {
            'login': courier_data['login'],
            'password': courier_data['password'],
            'firstName': courier_data.get('firstName')  # firstName не обязателен
        }
    return credentials


@pytest.fixture
def created_courier():
    """Фикстура для создания и последующего удаления курьера (для тестов авторизации)"""
    with allure.step('Генерировать данные курьера для логина'):
        courier_data = CourierGenerator.random_courier()
    with allure.step('Создать курьера для теста авторизации'):
        CourierHelper.create_courier(courier_data)

    yield courier_data

    with allure.step('Удалить курьера после теста авторизации'):
        CourierHelper.delete_courier(courier_data)


@pytest.fixture
def created_order():
    """Фикстура для создания заказа с автоматической отменой"""
    track_number = None

    with allure.step('Генерировать данные заказа'):
        order_data = OrderGenerator.random_order()

    with allure.step('Создать заказ'):
        response = OrderHelper.create_order(order_data)
        if response.status_code == STATUS_CREATED:
            track_number = response.json().get(FIELD_TRACK)

    yield {'order_data': order_data, 'track': track_number, 'response': response}

    if track_number:
        with allure.step(f'Отменить заказ (track={track_number})'):
            OrderHelper.cancel_order(track_number)