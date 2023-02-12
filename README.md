# Django Stripe API

Этот тестовое задание

**Описание**

stripe.com/docs (http://stripe.com/docs) - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей.

С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 

Мы предлагаем вам познакомиться с этой прекрасной платежной системой, реализовав простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров. 

Для решения нужно использовать Django. Решение бонусных задач даст вам возможность прокачаться и показать свои умения, но это не обязательно. 

**Задачи**

Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
* ~Django Модель Item с полями (name, description, price)~

API с двумя методами:

* ~GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса~

* ~GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)~

Пример реализации можно посмотреть в пунктах 1-3 тут (https://stripe.com/docs/payments/accept-a-payment?integration=checkout)

* ~Залить решение на Github, описать запуск в Readme.md~
* ~Опубликовать свое решение чтобы его можно было быстро и легко протестировать.~

Решения доступные только в виде кода на Github получат низкий приоритет при проверке.

Бонусные задачи: 

* ~Запуск используя Docker~
* ~Использование environment variables~
* ~Просмотр Django Моделей в Django Admin панели~
* ~Запуск приложения на удаленном сервере, доступном для тестирования~
* Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
* Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 
* Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
* Реализовать не Stripe Session, а Stripe Payment Intent.

## Развертывание

Клонируйте репозиторий:

`git clone https://github.com/kaminyv/django_stripe_api.git`

Прейдите в каталог проекта:

`cd django_stripe_api`

Скопируйте файл настроек

`cp app/.env.example app/.env`

Отредактируйте файл **.env**

`nano app/.env`

**Развертывание окружения без docker**

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

**Развертывание окружения c docker**

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

Соберите статичные файлы:

`docker exec -it django_stripe_api-app-1 python manage.py collectstatic`

Перезапустите docker

`docker compose restart`



