# 🐾 Vet-analytics-bot

> 🏥 *Система анализа ветеринарных данных от реальных врачей — для науки, статистики и заботы о собаках!*

  Анализ заболеваний собак по породе, возрасту и полу

---

## 📌 О проекте

Этот репозиторий содержит мой личный **pet-project**, который в данный момент находится в стадии активной разработки. 🚧

💡 Идея разработана мной лично.  
📊 Все данные предоставлены реальными ветеринарными врачами и основаны на **реальных клинических случаях**.

---

## 🎯 Цель проекта

Создать базу данных с информацией о собаках и провести анализ, чтобы выявить:

🔍 **Какие заболевания чаще всего встречаются у собак определённой породы, пола и возраста?**

---

## ✅ Задачи

| № | Задача | Статус |
|---|-------|--------|
| 1 | 🤖 Создать Telegram-бота для сбора данных от ветеринаров | ✅ |
| 2 | 💾 Разработать базу данных для хранения информации | ✅ |
| 3 | 📊 Провести статистический анализ заболеваемости | 🟡 |
| 4 | 📈 Сделать выводы и визуализировать результаты | 🔴 |

> 🟢 — выполнено  • 🟡 — в процессе  • 🔴 — не начато

---

## 🗂️ Структура репозитория

📁 **Основные файлы:**

- [`main.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/main.py) — 🚀 запуск бота
- [`handlers.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/handlers.py) — 🧩 обработчики команд
- [`keyboards.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/keyboards.py) — ⌨️ клавиатуры и кнопки
- [`middlewares.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/middlewares.py) — 📥 сохранение всех сообщений
- [`db.sqlite3`](https://github.com/Konvet/Vet-analytics-bot/blob/main/db.sqlite3) — 🗃️ база данных (SQLite)

📂 **Папка `app1/database`:**

- [`models.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/app1/database/models.py) — 🏗️ структура таблиц
- [`requests.py`](https://github.com/Konvet/Vet-analytics-bot/blob/main/app1/database/requests.py) — 🔁 функции для работы с БД


---

## 🛠️ Технологии

- 🐍 Python 3.13
- 🤖 [aiogram 3.x](https://docs.aiogram.dev) — для Telegram-бота
- 🗄️ SQLite — локальная база данных


<div align="center">
  <img src="https://img.shields.io/badge/Сделано_с_любовью-к_собакам-ff69b4?style=flat&logo=heart" alt="Made with love for dogs" />
  <br>
  <sub>🐶 Каждая строка кода — ради здоровья четвероногих друзей</sub>
</div>
