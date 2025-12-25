# Финальный проект Sprint 7 – Тестирование API Яндекс Самокат

## Описание проекта:
 В этом проекте протестировано API учебного сервиса Яндекс Самокат.  
 Документация API: [qa-scooter.praktikum-services.ru/docs](https://qa-scooter.praktikum-services.ru/docs/)

 Проект написан на **Python** с использованием **Pytest** и **Allure** для отчётности.

## Структура проекта

```
# Sprint_7/
│
├── tests/
│   ├── test_create_courier.py     # Тесты создания курьера
│   ├── test_login_courier.py      # Тесты авторизации курьера
│   ├── test_create_order.py       # Тесты создания заказов
│   └── test_order_list.py         # Тесты получения списка заказов
│
├── data/
│   ├──courier_generator          # Тестовые данные для курьера                    
│   ├── order_test_data.py         # Статус коды      
│   └── order_generator.py        # Генератор данных для заказов
│   ├── test_data.py               # Общие тестовые данные
├── helpers/
│   ├── courier_helper.py         # Хелпер для курьеров (создать/логин/удалить)
│   └── order_helper.py           # Хелпер для заказов (создать/получить список)
│
├── conftest.py                    # Фикстуры pytest
├── requirements.txt               # Зависимости проекта
└── README.md
├── urls.py                        # Базовые URL'ы сервиса
├── message.py                    # Сообщения об ошибках/ответах`


## Используемые технологии
 
 ```
### - **Python 3.11+**  
### - **Pytest** – фреймворк для тестирования  
### - **Requests** – для HTTP-запросов к API  
### - **Allure** – генерация отчётов по тестам 

## Установка и запуск

### 1. Клонировать репозиторий

```
git clone <URL_твоего_репозитория>
cd Sprint_7

### 2. Установить зависимости

```
pip install -r requirements.txt

### 3. Запустить тесты

```
pytest -v

## Генерация отчёта Allure

### 1. Запустить тесты с генерацией отчёта

```
pytest --alluredir=allure-results


### 2. Сформировать и открыть отчёт

```
allure serve allure-results
```
