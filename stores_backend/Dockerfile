# Используем базовый образ python
FROM python:3.12.2

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и приложение
COPY requirements.txt /app/
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Экспонируем порт 8000 для доступа к Django приложению
EXPOSE 8000

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]