# Habits tracker

Реализация бэкенд-части SPA веб-приложения. 

Трекер привычек с подключением телеграм-бота для рассылки уведомлений. 

## Стек технологий

- DRF
- Python
- PostgreSQL

## Инструкция по развертыванию

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/IliaPr/habits.git
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python3 -m venv venv
   # Для Linux/Mac
    source venv/bin/activate
   # Для Windows
    venv\Scripts\activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` на основе `.env.sample` и заполните его реальными значениями.

5. Выполните миграции:

    ```bash
    python3 manage.py migrate
    ```

6. Запустите сервер:

    ```bash
    python3 manage.py runserver
    ```

7. Откройте приложение в браузере по адресу http://127.0.0.1:8000/
