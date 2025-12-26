from faker import Faker

fake = Faker('ru_RU')


class CourierGenerator:
    @staticmethod
    def random_courier():
        """Генерирует случайные данные курьера с помощью faker"""
        return {
            'login': fake.user_name(),
            'password': fake.password(length=10, special_chars=True),
            'firstName': fake.first_name()
        }