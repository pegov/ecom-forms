# ecom-forms

Web-приложение для определения заполненных форм.

## Зависимости

- Python >=3.9

## Запуск 
```sh
# Создаём venv
python -m venv venv
# Активируем
. venv/bin/activate
# Устанавливаем зависимости
pip install -r requirements.txt	
# Тесты
python -m pytest
# Запускаем приложение
uvicorn --port 8080 app.main:app
# Скрипт для совершения тестовых запросов
python scripts/requests.py http://127.0.0.1:8080/get_form
```