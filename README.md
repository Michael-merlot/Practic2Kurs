# Описание проекта

# Job Parser
## Описание

Job Parser - это платформа для парсинга данных о соискателях и вакансиях с платформы hh.ru. Система позволяет получать информацию о вакансиях, сохранять её в базу данных и отображать статистику.
# Установка
## Клонирование репозитория
1. Сначала клонируйте репозиторий проекта на ваш локальный компьютер. Откройте терминал и выполните следующую команду:

`git clone (Ваш URL)`

## 2. Переход в директорию проекта.

Перейдите в директорию проекта:

`cd job_parser_project`

## 3. Создание и активация виртуального окружения.

Создайте и активируйте виртуальное окружение для изоляции зависимостей проекта:

`python -m venv env`

`env\Scripts\activate`
## 4. Установка зависимостей.

Установите зависимости, указанные в файле requirements.txt:

`pip install -r requirements.txt`

## 5. Настройка базы данных.

Настройте подключение к базе данных в файле settings.py. Убедитесь, что настройки соответствуют вашей локальной базе данных PostgreSQL.

### Пример настройки базы данных в settings.py:

# job_parser/settings.py

`DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'job_parser_db',
        'USER': 'job_parser_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}`
## 6. Применение миграций.

Примените миграции для создания необходимых таблиц в базе данных:

`python manage.py makemigrations parser_app`

`python manage.py migrate`

## 7. Создание суперпользователя.

Создайте суперпользователя для доступа к административной панели Django:

`python manage.py createsuperuser`

## 8. Использование

### Запустите сервер Django:

`python manage.py runserver`

## 9. Использование Docker

### Запустите контейнеры:

`docker-compose up --build`

Примените миграции:

`docker exec -it pythonproject6-web-1 python manage.py migrate`

Создайте суперпользователя:

`docker exec -it pythonproject6-web-1 python manage.py createsuperuser`

Откройте веб-браузер и перейдите по адресу http://localhost:8000.

## 10. Доступ к административной панели.

Перейдите по адресу http://localhost:8000/admin/ и войдите под учетной записью суперпользователя для управления данными в базе.

## 11. Доступ к веб-интерфейсу.

### Перейдите в веб-браузер и откройте следующие адреса:

Для получения и отображения вакансий: http://localhost:8000/parser/fetch-jobs/

Для просмотра статистики вакансий: http://localhost:8000/parser/job-statistics/


## 12. Документация API.

### Эндпоинты:

GET /parser/fetch-jobs/ - Получение и отображение вакансий.

GET /parser/job-statistics/ - Отображение статистики вакансий.

## 13. Тестирование

### Написание тестов.

В проекте уже настроены базовые юнит-тесты для моделей и представлений. Вы можете найти их в файле parser_app/tests.py.

### Запуск тестов.

Для запуска тестов выполните следующую команду:

`python manage.py test`

Убедитесь, что все тесты проходят успешно. Это гарантирует, что ваша система работает корректно.