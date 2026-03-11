@echo off
chcp 65001 >nul

echo ============================
echo Запуск всех сервисов проекта
echo ============================

start "SERVER 8001" cmd /k ".\.venv\Scripts\python.exe -m uvicorn server.server:app --reload --host 127.0.0.1 --port 8001"

start "WS SERVICE 8002" cmd /k ".\.venv\Scripts\python.exe -m uvicorn ws_service.ws_service:app --reload --host 127.0.0.1 --port 8002"

start "CLIENT 8003" cmd /k ".\.venv\Scripts\python.exe -m uvicorn client.server:app --reload --host 127.0.0.1 --port 8003"

start "CADDY PROXY 8080" cmd /k ".\reverse_proxy\caddy_windows_amd64.exe run --config .\reverse_proxy\Caddyfile --adapter caddyfile"

echo.
echo Все сервисы запущены.
echo Открой в браузере:
echo http://theme.test:8080/
pause