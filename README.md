# Vet-analytics-bot

Этот репозиторий содержит мой личный pet-project. На данный момент он пока что в стадии реализации и не завершён.

Идея данного проекта была разработана мной лично. Данные получены от реальных ветеринарных врачей и включают реальные клинические случаи.

## Цель проекта
Создать базу данных с домашними питомцами (собаками) для дальнейшего анализа и подведения итогов по распространённости заболеваний среди групп собак одной породы, пола и возраста.

## Задачи
1. Создать Telegram-бота для сбора информации о животных от ветеринарных врачей.
2. Создать базу данных для хранения информации.
3. Провести статистический анализ частоты встречаемости заболеваний среди определённых групп собак (по породе, возрасту и полу).
4. Сделать выводы на основе анализа.

## Содержание репозитория
- [`main.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/main.py) — основной файл, запускающий все процессы Telegram-бота.
- [`handlers.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/handlers.py) — обработчики всех функций бота.
- [`keyboards.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/keyboards.py) — код для создания клавиатур в боте.
- Папка `app1`:
  - [`models.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/app1/database/models.py) — структура базы данных.
  - [`requests.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/app1/database/requests.py) — функции для выполнения запросов к базе данных.
- [`middlewares.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/middlewares.py) — middleware для сохранения всех входящих сообщений в бот.
- [`db.sqlite3`](https://github.com/Konvet/Vet-analytics-bot/blob/main/db.sqlite3) — файл базы данных (SQLite).
