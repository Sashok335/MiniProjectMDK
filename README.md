# Угадай число

Консольная игра, в которой компьютер загадывает число от -100 до 100, а пользователь его угадывает.
Результаты сохраняются в SQLite, ведётся таблица лидеров.

## Установка и запуск

```bash
pip install -r requirements.txt
python main.py
```

## Тестирование

```bash
pytest tests/ -v
pytest tests/ --cov=. -v
```

## Архитектура

```
main.py        — точка входа, консольное меню
game.py        — бизнес-логика (генерация числа, проверка, игровой цикл)
database.py    — работа с SQLite (инициализация, сохранение, получение рекордов)
tests/         — модульные тесты (pytest)
```

### Схема взаимодействия

```
Пользователь → main.py (меню)
                ├── Новая игра → game.py → database.py → SQLite
                └── Таблица лидеров → database.py → SQLite
```

### База данных

Таблица `records`:
- `id` — INTEGER PRIMARY KEY AUTOINCREMENT
- `nickname` — TEXT NOT NULL
- `attempts` — INTEGER NOT NULL
- `date` — TIMESTAMP DEFAULT CURRENT_TIMESTAMP
