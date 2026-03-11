# Practicum
Practicum — ЛР1: Микросервисная архитектура (FastAPI + WebSocket + Reverse Proxy)
Стек

Python 3.10+

FastAPI

Uvicorn

htpy

Reverse proxy: Caddy

Структура проекта

server/ — сервер №1 (GET /, проверка Accept: text/html, HTML-страница с темой + ссылка на client)

ws_service/ — WebSocket-сервис (/ws), периодические сообщения + обработка уникальных сообщений

client/ — сервер-клиент (GET /, HTML + подключение JS)

client/static/app.js — JS-логика (WebSocket, обновление DOM, кнопка)

reverse_proxy/ — Caddy + Caddyfile

Установка зависимостей

Открыть PowerShell в корне проекта:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Запуск без reverse proxy (проверка по портам)

Открыть 3 терминала (или вкладки терминала) в корне проекта и запустить:

1) server (порт 8001)
.\.venv\Scripts\Activate.ps1
python -m uvicorn server.server:app --reload --host 127.0.0.1 --port 8001
2) ws_service (порт 8002)
.\.venv\Scripts\Activate.ps1
python -m uvicorn ws_service.ws_service:app --reload --host 127.0.0.1 --port 8002
3) client (порт 8003)
.\.venv\Scripts\Activate.ps1
python -m uvicorn client.server:app --reload --host 127.0.0.1 --port 8003
Проверка (без прокси)

server: http://127.0.0.1:8001/

client: http://127.0.0.1:8003/

WS вручную в браузере как страницу не открывается (это нормально), WebSocket endpoint: ws://127.0.0.1:8002/ws

Настройка reverse proxy (Caddy) — пункт 8–9
1) hosts (придуманные адреса)

Открыть файл hosts от администратора:
C:\Windows\System32\drivers\etc\hosts

Добавить в конец:

127.0.0.1 theme.test
127.0.0.1 client.test
127.0.0.1 ws.test

Сброс DNS:

ipconfig /flushdns

Проверка:

ping theme.test
ping client.test
ping ws.test
2) Caddy

Скачать caddy.exe (Windows amd64) и положить в reverse_proxy/ (файл не коммитится, он в .gitignore).

4) Запуск Caddy

Отдельный терминал в корне проекта:

.\reverse_proxy\caddy_windows_amd64.exe run --config .\reverse_proxy\Caddyfile --adapter caddyfile

Если имя файла другое (например caddy.exe) — заменить в команде.

Запуск через reverse proxy (итоговая схема)

Запустить server на 8001

Запустить ws_service на 8002

Запустить client на 8003

Запустить Caddy (проксирует на 8080)

Проверка через прокси

server: http://theme.test:8080/

client: http://client.test:8080/

WebSocket в клиенте должен подключаться к:

ws://ws.test:8080/ws

Что считается корректной работой
server (theme)

открывается http://theme.test:8080/

отображается тема

есть ссылка на client (http://client.test:8080/)

client

открывается http://client.test:8080/

есть элементы h1, пустой h2, пустой p, кнопка

JS подключён (/static/app.js отдаётся без 404)

после WebSocket handshake h2 заполняется, кнопка активируется

p обновляется сообщениями от WS сервиса каждые 2–5 секунд

по нажатию кнопки отправляется уникальное сообщение, сервер отвечает:
Да? Хорошо. Спасибо за поддержку!

Частые ошибки и решения
502 Bad Gateway в браузере

Caddy не может достучаться до внутренних портов.

проверить, что сервисы реально запущены на 8001/8002/8003

проверить netstat -ano | findstr :8003 (должен быть LISTENING)

перезапустить Caddy после правок Caddyfile

Client sent an HTTP request to an HTTPS server

Caddy включил HTTPS.

использовать auto_https off в Caddyfile (как в конфиге выше)

перезапустить Caddy

window.WS_URL = undefined

Открыта не та страница или не та версия HTML/JS.

проверить http://client.test:8080/static/app.js (должен отдаваться)

в DevTools Console проверить window.WS_URL