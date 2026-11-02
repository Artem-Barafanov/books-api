# Docker Homework

Приложение состоит из двух Docker-контейнеров:

- app — Python Flask API.
- db — база данных PostgreSQL 16.

Контейнеры взаимодействуют через сеть books_network.

Для сохранения данных используется Docker Volume
postgres_data.

## Требования

- Docker Desktop
- Docker Compose

## Запуск

Склонировать репозиторий.

Перейти в папку проекта:

cd books-api

Собрать и запустить контейнеры:

docker compose up --build -d

## Проверка

Проверить состояние контейнеров:

docker compose ps

Открыть главную страницу:

http://localhost:5000/

Получить список книг из базы данных:

http://localhost:5000/books

## Проверка сохранности данных

Остановить и удалить контейнеры:

docker compose down

Запустить повторно:

docker compose up -d

Открыть:

http://localhost:5000/books

## Остановка

docker compose down
