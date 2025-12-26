import requests
import allure
from urls import OrderUrls


class OrderHelper:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        with allure.step('POST /api/v1/orders'):
            return requests.post(OrderUrls.CREATE_ORDER, json=order_data)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_orders():
        with allure.step('GET /api/v1/orders'):
            return requests.get(OrderUrls.GET_ORDERS)

    @staticmethod
    @allure.step('Отмена заказа')
    def cancel_order(track):
        with allure.step(f'PUT /api/v1/orders/cancel (track={track})'):
            return requests.put(OrderUrls.CANCEL_ORDER, json={'track': track})