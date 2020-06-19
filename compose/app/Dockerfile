FROM python:3.8.0-alpine3.10

ENV USR_LOCAL_BIN=/usr/local/bin/  \
    PROJECT_ROOT=/app

# путь до исходников
ENV PYTHONPATH=$PYTHONPATH:$PROJECT_ROOT

# пакеты, которые необходимы для работы в runtime
ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    postgresql-dev \
    libmagic \
    libjpeg \
	python-dev \
	libxml2 \
	libxml2-dev \
	libxslt-dev

# Пакеты, которые необходимы для установки зависимостей.
# Не останутся в итоговом образе.
ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers \
    libc-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev

# Создание директорий
RUN mkdir $PROJECT_ROOT/ && \
    mkdir $PROJECT_ROOT/run && \
    mkdir $PROJECT_ROOT/wsgi

COPY ./Pipfile ./Pipfile.lock $PROJECT_ROOT/
WORKDIR $PROJECT_ROOT

# Установка зависимостей
RUN pip install --upgrade wheel pip pipenv==2018.11.26 \
    && apk --no-cache add --virtual build-deps $BUILD_PACKAGES \
    && apk --no-cache add $RUNTIME_PACKAGES \
    && set -ex && pipenv install --deploy --system --dev \
    # Удаление ненужных пакетов
    && apk del build-deps

# копирование непосредственно проекта
COPY ./src $PROJECT_ROOT

COPY ./compose/app/start_uwsgi $USR_LOCAL_BIN/

RUN sed -i 's/\r//' $USR_LOCAL_BIN/start_uwsgi \
    && chmod +x $USR_LOCAL_BIN/start_uwsgi

COPY ./compose/app/uwsgi.ini $PROJECT_ROOT/wsgi

EXPOSE 8000

CMD ["start_uwsgi"]
