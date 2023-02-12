# Django Stripe API

## Развертывание

Клонируйте репозиторий:

`git clone https://github.com/kaminyv/django_stripe_api.git`

Прейдите в каталог проекта:

`cd django_stripe_api`

Скопируйте файл настроек

`cp app/.env.example app/.env`

Отредактируйте файл **.env**

`nano app/.env`

### Развертывание окружения без docker

Создайте виртуальное окружение:

`python3 -m venv venv`

Активируйте виртуальное окружение:

`source venv/bin/activate`

Обновите pip:

`pip install --upgrade pip`

Установите модули для проекта:

`pip install -r requirements.txt`

Соберите миграции:

`python app/manage.py makemigrations`

Примените миграции:

`python app/manage.py migrate`

Примените тестовые данные:

`python app/manage.py createdata`

Создайте суперпользователя:

`python app/manage.py createsuperuser`

Запустите тестовый сервер:

`python app/manage.py runserver`

### Развертывание окружения c docker

Запустите сборку docker

`docker compose up -d`

Соберите миграции:

`docker exec -it django_stripe_api-app-1 python manage.py makemigrations`

Примените миграции:

`docker exec -it django_stripe_api-app-1 python manage.py migrate`

Примените тестовые данные:

`docker exec -it django_stripe_api-app-1 python manage.py createdata`

Создайте суперпользователя:

`docker exec -it django_stripe_api-app-1 python manage.py createsuperuser`

Перезапустите docker

`docker compose restart`



