import pytest
import allure
from data.order_generator import OrderGenerator
from data.order_test_data import FIELD_TRACK, STATUS_CREATED


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @allure.description('Проверка: один цвет (BLACK/GREY), оба цвета или без цвета; в ответе есть track')
    @pytest.mark.parametrize(
        'color',
        [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            None,
        ]
    )
    @allure.feature('Создание заказа')

    def test_create_order_with_black_color(self, created_order):
        """Тест создания заказа с цветом BLACK"""
        created_order['order_data']['color'] = ['BLACK']
        response = created_order['response']
        assert response.status_code == STATUS_CREATED, f"Ожидался код {STATUS_CREATED}, получен {response.status_code}"
        body = response.json()
        assert FIELD_TRACK in body, f"В ответе отсутствует поле '{FIELD_TRACK}'"
        assert isinstance(body[FIELD_TRACK], int), f"Поле '{FIELD_TRACK}' должно быть числом"

    @allure.title('Создание заказа с цветом GREY')
    @allure.description('Проверка создания заказа с одним цветом (GREY)')
    def test_create_order_with_grey_color(self, created_order):
        """Тест создания заказа с цветом GREY"""
        created_order['order_data']['color'] = ['GREY']
        response = created_order['response']
        assert response.status_code == STATUS_CREATED, f"Ожидался код {STATUS_CREATED}, получен {response.status_code}"
        body = response.json()
        assert FIELD_TRACK in body, f"В ответе отсутствует поле '{FIELD_TRACK}'"
        assert isinstance(body[FIELD_TRACK], int), f"Поле '{FIELD_TRACK}' должно быть числом"

    @allure.title('Создание заказа с цветами BLACK и GREY')
    @allure.description('Проверка создания заказа с двумя цветами (BLACK, GREY)')
    def test_create_order_with_black_and_grey_colors(self, created_order):
        """Тест создания заказа с цветами BLACK и GREY"""
        created_order['order_data']['color'] = ['BLACK', 'GREY']
        response = created_order['response']
        assert response.status_code == STATUS_CREATED, f"Ожидался код {STATUS_CREATED}, получен {response.status_code}"
        body = response.json()
        assert FIELD_TRACK in body, f"В ответе отсутствует поле '{FIELD_TRACK}'"
        assert isinstance(body[FIELD_TRACK], int), f"Поле '{FIELD_TRACK}' должно быть числом"

    @allure.title('Создание заказа без указания цвета')
    @allure.description('Проверка создания заказа без цвета')
    def test_create_order_without_color(self, created_order):
        """Тест создания заказа без указания цвета"""
        created_order['order_data'].pop('color', None)
        response = created_order['response']
        assert response.status_code == STATUS_CREATED, f"Ожидался код {STATUS_CREATED}, получен {response.status_code}"
        body = response.json()
        assert FIELD_TRACK in body, f"В ответе отсутствует поле '{FIELD_TRACK}'"
        assert isinstance(body[FIELD_TRACK], int), f"Поле '{FIELD_TRACK}' должно быть числом"
