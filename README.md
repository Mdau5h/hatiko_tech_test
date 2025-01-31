# Тестовое задание для Хатико-Техника.

## Подготовка проекта
- Установить Python 3.11:
https://www.python.org/downloads/

- Проверить версию Python
```sh
python3 --version
```
- Перейти в директорию проекта
- Установить зависимости
```sh
pip install -U pip setuptools pipenv && pipenv install
 ```
- Создать файл `.env` в котором будут перечислены:
  - `CHECK_API_URL` - URL сервиса проверки IMEI
  - `CHECK_API_TOKEN` - токен авторизации сервиса проверки IMEI
  - `BOT_TOKEN` - токен telegram-бота
  - `WEBHOOK_URL` - URL сервера для отправки веб-хуков
  - `DB_NAME` - база с белым списком
 
- Создать файл `{DB_NAME}.db` в котором будут перечислены telegram ID пользователей, входящих в белый список

## Запуск проекта
- Запустить команду:
```sh
pipenv run python3 asgi.py
```
