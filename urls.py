class BaseUrls:
    BASE_URL = "http://qa-scooter.praktikum-services.ru"                        # Основной сайт


class CourierUrls:
    CREATE_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier"                      #Ручка на создание курьера 
    LOGIN_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier/login"                 #Ручка на проверку логина курьера в системе 
    DELETE_COURIER = f"{BaseUrls.BASE_URL}/api/v1/courier/{{courier_id}}"       #Ручка на удаления курьера, динамическая 


class OrderUrls:
    CREATE_ORDER = f"{BaseUrls.BASE_URL}/api/v1/orders"                         #Ручка на создание заказа )
    GET_ORDERS = f"{BaseUrls.BASE_URL}/api/v1/orders"                           #Ручка на получение списка заказов 
    CANCEL_ORDER = f"{BaseUrls.BASE_URL}/api/v1/orders/cancel"                  #Ручка на отмену заказа 