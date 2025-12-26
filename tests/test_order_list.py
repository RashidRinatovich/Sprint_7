import allure
from helpers.order_helper import OrderHelper
from data.order_test_data import FIELD_ORDERS, STATUS_OK


@allure.feature('Получение списка заказов')
class TestOrderList:

    @allure.title('В теле ответа возвращается список заказов')
    @allure.description('Проверка, что эндпоинт возвращает список заказов в поле orders')
    def test_get_orders_returns_list(self):
        """Тест проверяет, что в теле ответа возвращается список заказов"""
        with allure.step('Отправить запрос на получение списка заказов'):
            response = OrderHelper.get_orders()

        with allure.step('Проверить код ответа 200'):
            assert response.status_code == STATUS_OK, f"Ожидался код {STATUS_OK}, получен {response.status_code}"

        with allure.step('Проверить, что поле orders присутствует и это список'):
            response_data = response.json()
            assert FIELD_ORDERS in response_data, f"В ответе отсутствует поле '{FIELD_ORDERS}'"
            assert isinstance(response_data[FIELD_ORDERS], list), f"Поле '{FIELD_ORDERS}' должно быть списком"