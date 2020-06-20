![CI](https://github.com/GoddessEyes/gpb_backend/workflows/CI/badge.svg)
![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge)

# You are breathtaking !!!

## Вы великолепны !!!

![You are breathtaking](https://memepedia.ru/wp-content/uploads/2019/06/keanu-meme.jpg)


```text
Сервис является базовой реализацией системы публикации идей.
Модули:
  1. Регистрация/авторизация.
  2. Публикация идей.
  3. Модерация сервиса.
  4. Голосование за идеи.
  5. Комментирование идей. 
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

