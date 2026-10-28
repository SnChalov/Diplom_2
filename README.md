
# Stellar Burgers — API и UI тесты

Проект автоматизированного тестирования учебного приложения Stellar Burgers.

## Технологии

 Python
 pytest
 Requests
 Selenium
 Allure
 
## Установка и запуск

Клонируйте репозиторий и перейдите в папку проекта.

Установите зависимости:

pip install -r requirements.txt

Запустите API-тесты:

python -m pytest tests/api -v

## Allure-отчёт

Запустите тесты с сохранением результатов:

python -m pytest tests/api --alluredir=allure-results

Сгенерируйте отчёт:

allure generate allure-results -o allure-report --clean

Откройте отчёт в браузере:

allure open allure-report

## Структура проекта

 `data/` — URL и тестовые данные.
 `tests/api/` — API-тесты.
 `tests/ui/` — UI-тесты.
 `helpers/` — вспомогательные функции.
 `conftest.py` — фикстуры pytest.
 `requirements.txt` — зависимости проекта.
