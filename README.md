# 🐘 Slonik API

Backend API для сервиса фотосалона **Слоник**.

Проект предоставляет REST API для управления пользователями, услугами, корзиной и заказами.

## 🚀 Возможности

- Регистрация и авторизация пользователей
- JWT-аутентификация
- Разделение прав пользователей и администратора
- Управление услугами
- Работа с корзиной
- Создание и управление заказами
- Асинхронная работа с базой данных
- Покрытие проекта тестами

---

## 🛠 Технологии

- Python 3.12
- FastAPI
- SQLAlchemy 2.0 (Async)
- PostgreSQL 16
- Docker
- Pydantic v2
- JWT (python-jose)
- Passlib + bcrypt
- Pytest

---

## 📁 Структура проекта

```
Slonik API
│
├── app
│   ├── api          # API маршруты
│   ├── core         # настройки, безопасность, зависимости
│   ├── db           # подключение базы данных
│   ├── models       # SQLAlchemy модели
│   ├── repositories # слой работы с БД
│   ├── schemas      # Pydantic схемы
│   ├── services     # бизнес-логика
│   └── main.py
│
├── tests            # тесты проекта
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Запуск проекта

## 1. Клонирование проекта

```bash
git clone <repository-url>

cd Photocentr-api
```

---

## 2. Создание виртуального окружения

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

## 4. Настройка переменных окружения

Создать файл `.env`:

```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/slonik_db

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# 🐳 Запуск PostgreSQL через Docker

Запуск базы:

```bash
docker compose up -d
```

Проверка контейнера:

```bash
docker ps
```

После запуска будет доступен PostgreSQL:

```
localhost:5432
```

---

# ▶️ Запуск приложения

```bash
uvicorn app.main:app --reload
```

После запуска документация доступна:

Swagger:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 🧪 Тестирование

Запуск тестов:

```bash
pytest
```

Запуск с покрытием:

```bash
pytest --cov=app --cov-report=term-missing
```

Текущий результат:

```
56 passed

Coverage: ~75%
```

---

# 🔐 Аутентификация

В проекте используется JWT.

Основные возможности:

- регистрация пользователя
- вход в систему
- получение текущего пользователя
- проверка прав администратора

---

# 👤 Роли пользователей

### Пользователь

Может:

- просматривать услуги
- работать с корзиной
- создавать заказы


### Администратор

Может:

- создавать услуги
- изменять услуги
- удалять услуги

---

# 📌 API разделы

Основные маршруты:

```
/api/v1/users
/api/v1/services
/api/v1/cart
/api/v1/orders
```

---

# 📦 Docker

Используется PostgreSQL контейнер:

```
postgres:16
```

Имя контейнера:

```
slonik_db
```

---

# 📄 Лицензия

Учебный дипломный проект.
