from faker import Faker

fake = Faker('ru_RU')


class OrderGenerator:
    @staticmethod
    def random_order(color=None):
        """Генерирует случайные данные заказа с помощью faker"""
        order_data = {
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'address': fake.address(),
            'metroStation': fake.random_int(min=1, max=237),
            'phone': fake.phone_number(),
            'rentTime': fake.random_int(min=1, max=7),
            'deliveryDate': fake.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
            'comment': fake.sentence()
        }

        if color is not None:
            order_data['color'] = color

        return order_data