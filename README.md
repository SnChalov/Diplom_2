# Stellar Burgers — API и UI тесты

Проект автоматизированного тестирования приложения Stellar Burgers

## Технологии

  Python
  pytest
  Requests
  Selenium
  Allure

## Установка и запуск

Клонируйте репозиторий и перейдите в папку проекта

Установите зависимости:

pip install -r requirements.txt

## API-тесты

Запуск API-тестов:

python -m pytest tests/api -v

## UI-тесты

UI-тесты проверяют основные функции приложения Stellar Burgers:

  Переход между разделами «Конструктор» и «Лента заказов».
  Открытие и закрытие модального окна ингредиента.
  Увеличение счётчика ингредиента при добавлении в заказ.
  Увеличение счётчиков выполненных заказов после создания заказа.
  Отображение номера созданного заказа в разделе «В работе». 
Тесты запускаются в браузерах Chrome и Firefox.

Запуск UI-тестов:

bash
python -m pytest tests/ui -v

## Запуск всех тестов

python -m pytest -v

## Allure-отчёт

Запустите все тесты с сохранением результатов:

python -m pytest --alluredir=allure-results

Сгенерируйте отчёт:

allure generate allure-results -o allure-report --clean

Откройте отчёт в браузере:

allure open allure-report

## Структура проекта

  `data/` — URL и тестовые данные.
  `tests/api/` — API-тесты.
  `tests/ui/` — UI-тесты.
  `pages/` — Page Object классы для UI-тестов.
  `locators/` — локаторы элементов интерфейса.
  `helpers/` — вспомогательные функции.
  `conftest.py` — фикстуры pytest.
  `requirements.txt` — зависимости проекта.