@echo off
echo Starting Amanawit Design Servers...
echo.

echo Starting Backend Server...
cd /d "c:/Users/NAWAB/Desktop/amanawit design - Copy/backend"
start "Backend Server" cmd /k "python manage.py runserver 127.0.0.1:8000"

echo Starting Frontend Server...
cd /d "c:/Users/NAWAB/Desktop/amanawit design - Copy"
start "Frontend Server" cmd /k "python -m http.server 8081 --bind 127.0.0.1"

echo.
echo Both servers are starting...
echo Backend: http://127.0.0.1:8000
echo Frontend: http://127.0.0.1:8081
echo.
pause
