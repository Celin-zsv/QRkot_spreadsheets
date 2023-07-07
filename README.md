[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=F71329&multiline=true&width=435&lines=+QRkot_spreadseets)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=1D39F7&multiline=true&width=435&lines=+QRkot_spreadseets)](https://git.io/typing-svg)  
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=15&duration=2000&pause=1000&color=1FBB30F6&multiline=true&width=435&lines=+QRkot_spreadseets)](https://git.io/typing-svg)    
[![Typing SVG](https://img.shields.io/badge/QRkot_spreadseets-sprint--23%20ver.2-red)](https://git.io/typing-svg)

### Проект: QRkot_spreadseets. Спринт-23, ver.2, Зеленковский Сергей  
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
![](https://cdn-icons-png.flaticon.com/128/104/104068.png)
![]()
![](https://www.sqlalchemy.org/img/sqla_logo.png)

#### Содержание
1. [Описание проекта](#Описание-проекта)
2. [Установка](#Установка)
3. [Запуск](#Запуск)
4. [Структура проекта](#структура-проекта)
***
### 1. *Описание проекта*


Parameter  | Value
-------------|:-------------
Наименование проекта  | QRKot
Назначение проекта | Сервис благотворительного фонда по сбору пожервований . Интерфейс: api, Google spreadsheets.
Tech Stack. Client. OS | Windows, Linux, MacOS
Tech Stack. Project |[Python v.3.9 и выше](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/), [FastAPI Users](https://fastapi-users.github.io/fastapi-users/), [SQLAlchemy](https://pypi.org/project/SQLAlchemy/), [Alembic](https://alembic.sqlalchemy.org/), [Google Sheets](https://www.google.ru/intl/ru/sheets/about/)
GitHub | https://github.com/Celin-zsv/cat_charity_fund
Author | Sergei Zelenkovskii, svzelenkovskii@gmail.com  

### 2. *Установка*
2.1. клонировать репозиторий
```
cd dev
git@github.com:Celin-zsv/QRkot_spreadsheets.git
cd QRkot_spreadsheets
```
2.2. создать и активировать виртуальное окружение:
```
  # Windows
python -m venv env
. env/Scripts/activate
  # Unix / MacOS
python3 -m venv env
source venv/bin/activate
```
2.3. обновить менеджер пакетов pip, установить зависимости requirements.txt:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
2.4. создать в корне файл .env + наполнить:
```
touch .env
```
```
APP_TITLE=<наименование сервиса>
APP_DESCRIPTION=<описание сервиса>
DATABASE_URL=<настройки подключения к БД, например: sqlite+aiosqlite:///./fastapi.db>
SECRET=<секретный ключ>
FIRST_SUPERUSER_EMAIL=<email первого суперпользователя>
FIRST_SUPERUSER_PASSWORD=<пароль первого суперпользователя>
# Переменные ниже для формирования отчёта Google Sheets, 
# предварительно требуются создать сервисный аккаунт Google Cloud Platform.
EMAIL=<USER_EMAIL>
TYPE=service_account
PROJECT_ID=<PROJECT_ID>
PRIVATE_KEY_ID=<PRIVATE_KEY_ID>
PRIVATE_KEY=<PRIVATE_KEY>
CLIENT_EMAIL=<CLIENT_EMAIL>
CLIENT_ID=<CLIENT_ID>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<CLIENT_ID>
```
2.5. применить миграции
```
alembic upgrade head
```

### 3.
## Запуск

3.1. запустить проект -> ввести команду: локально старт проекта
```
uvicorn app.main:app --reload
```
3.2. документация:
* Swagger [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/redoc)
* содержит:
  * доступные эндпоинты
  * примеры запросов
  * варианты ответов
  * возможные ошибки

3.3. при первом запуске проекта создается суперпользователь (см.переменные в .env): использовать данные суперпользователя для авторизации пользователя в Swagger

3.4. Отчеты Google Sheets:
* /google - получение отчета о закрытых проектах в формате Google Sheets

### 4. *Структура проекта*
```
cat_charity_fund:
    ├── app
    │   ├── api
    │   │   ├── endpoints
    │   │   │   ├── __init__ .py
    │   │   │   ├── charity_project.py
    │   │   │   ├── donation.py
    │   │   │   └── user.py
    │   │   ├── __init__ .py
    │   │   ├── routers.py
    │   │   └── validators.py
    │   ├── core
    │   │   ├── __init__ .py
    │   │   ├── base.py
    │   │   ├── config.py
    │   │   ├── db.py
    │   │   ├── init_db.py
    │   │   └── user.py
    │   ├── crud
    │   │   ├── __init__ .py
    │   │   ├── base.py
    │   │   ├── charity_project.py
    │   │   └── donation.py
    │   ├── models
    │   │   ├── __init__ .py
    │   │   ├── charity_project.py
    │   │   ├── donation.py
    │   │   └── user.py
    │   ├── schemas
    │   │   ├── __init__ .py
    │   │   ├── charity_project.py
    │   │   ├── donation.py
    │   │   └── user.py
    │   ├── services
    │   │  ├── __init__ .py
    │   │  └── investment.py
    │   ├── __init__.py
    │   └── main.py
```



@zsv
