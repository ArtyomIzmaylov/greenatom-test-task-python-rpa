# Проект FastAPI и SQLite

Тестовое задание на позицию Python RPA, Компания Greenatom

## Установка

1. git clone https://github.com/yourusername/yourrepository.git
2. pip install -r requirements.txt

## Запууск
uvicorn main:app --reload

## Тестирование

1. Swagger - http://127.0.0.1:8000/docs
2. `/start_robot/{start_number:int}` - Эндпоинт для запуск робота
3. `/stop_robot` - Эндпоинт для остановки робота
4. `/runs` - Эндпоинт для получения информации о id, start_number, start_time(время запуска), duration(длительность)
