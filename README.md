# Описание
Проект "API для социальной сети Yatube" представляет собой RESTful API, разработанный с использованием Django и Django REST framework. Это API позволяет пользователям создавать, просматривать и взаимодействовать с постами, комментариями, группами и подписками. API обеспечивает безопасную аутентификацию пользователей с использованием токенов, что гарантирует сохранность и конфиденциальность пользовательских данных.

# Установка

1. Клонируйте репозиторий на свой компьютер:

git@github.com:SHURSHALO/api_final_yatube.git

2. Создайте и активируйте виртуальное окружение:

python -m venv venv

venv\Scripts\activate

3. Установите зависимости:

pip install -r requirements.txt

4. Примените миграции:

python manage.py migrate

5. Создайте суперпользователя:

python manage.py createsuperuser

6. Запустите сервер разработки:

python manage.py runserver