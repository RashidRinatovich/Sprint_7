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
    def test_create_order_with_different_colors(self, color, created_order):
        """Тест создания заказа с разными вариантами цвета"""
        # Обновляем order_data цветом из параметра
        with allure.step(f'Обновить данные заказа цветом: {color}'):
            created_order['order_data']['color'] = color

        with allure.step('Проверить код ответа 201'):
            response = created_order['response']
            assert response.status_code == STATUS_CREATED, f"Ожидался код {STATUS_CREATED}, получен {response.status_code}"

        with allure.step("Проверить, что в ответе есть поле 'track' (int)"):
            body = response.json()
            assert FIELD_TRACK in body, f"В ответе отсутствует поле '{FIELD_TRACK}'"
            assert isinstance(body[FIELD_TRACK], int), f"Поле '{FIELD_TRACK}' должно быть числом"