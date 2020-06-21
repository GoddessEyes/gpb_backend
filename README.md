![CI](https://github.com/GoddessEyes/gpb_backend/workflows/CI/badge.svg)
![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)

# You are breathtaking !!!

![You are breathtaking](https://memepedia.ru/wp-content/uploads/2019/06/keanu-meme.jpg)

```text
Уникальность:
Виртуальный помощник маскот, удобное мобильное приложение для легкости и простоты использования,
уникальная геймифицированная система вовлечения и удержания пользователей - 
пользователь двигается по 4 ролям -сотрудник, активист, эксперт, рационализатор, 
выполняет задания и за набранные поинты выбирает товары в корпоративном магазине
```

```text
Обратите внимание на репозитории: 

  Frontend: https://github.com/Hvoya/gpb-frontend
  Mobile: https://github.com/bigman212/DigitalHackaton_2
  Design: https://xd.adobe.com/view/59ebe566-5d60-4d4b-4245-8f1300911a0c-2fda/
```

|       Ключ        |     Значение     |  
|-------------------|------------------|
|`AUTH_LDAP_SERVER_URI`| Сервер LDAP |
|`AUTH_LDAP_BIND_DN`| ??? |
|`AUTH_LDAP_BIND_PASSWORD`| ??? | 
|`AUTH_LDAP_GROUP_SEARCH`| ??? | 
|`AUTH_LDAP_GROUP_TYPE`| ??? |
|`AUTH_LDAP_REQUIRE_GROUP`| ??? |
|`AUTH_LDAP_DENY_GROUP`| ??? |


```text
Сервис является базовой реализацией системы публикации идей.
Модули:
  1. Регистрация/авторизация.
  2. Публикация идей.
  3. Модерация сервиса.
  4. Голосование за идеи.
  5. Комментирование идей.
  6. Предложение бизнес решения.
      6.1. Бизнес решения для идеи.
      6.2. Бизнес решения одиночно.
  7. Статистика пользователя.
```

#### Django:
1) Склонировать проект себе.
```bash
git clone https://github.com/GoddessEyes/gpb_backend.git
```
2) Создать`.env` файл и настроить проект. Пример настроек в `.env.example`.
```bash
touch .env
```
3) Активировать окружение.  Все переменные окружения подгрузятся в сессию шела автоматически из `.env`
```bash 
pipenv shell
```
4) Накатить миграции 
```bash
 python src/manage.py migrate
```
5) Запустить сервер 
```bash
 python src/manage.py runserver
```

### Запуск "production" сборки

```bash 
docker-compose up --build -d
```

__Команда для создания суперпользователя в запущеном контейнере:__

```bash
docker-compose exec app /usr/local/bin/python manage.py createsuperuser
```

