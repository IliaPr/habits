# официальный образ Python
FROM python:3

# Установка зависимостей
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Копирование кода приложения
COPY . /app/

# CMD для запуска Celery и основного приложения
CMD ["bash", "-c", "service redis-server start && celery -A celery worker --loglevel=info && python3 manage.py runserver 0.0.0.0:8000"]
