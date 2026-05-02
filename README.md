# Лабораторная работа №5 (CI, GitHub Actions)

Проект на Python с unit-тестами и CI через GitHub Actions
Основа проекта - Лабораторная работа №4 

Файл `rectangle.py` содержит:
- функции `area(a, b)` и `perimeter(a, b)` для вычисления площади и периметра прямоугольника;
- класс `RectangleTestCase` с unit-тестами на базе `unittest`.

## Запуск тестов

```bash
python3 -m unittest rectangle.py
```

## CI на GitHub Actions

При каждом `push` в репозиторий автоматически запускается workflow `main.yml`, который:

- выполняется на двух встроенных runner’ах: `ubuntu-latest` и `windows-latest`;
- чекаутит репозиторий;
- устанавливает Python 3.x;
- запускает модульные тесты командой:

```bash
python -m unittest rectangle.py
```

## Структура проекта

```text
.
├── rectangle.py
├── README.md
└── .github
    └── workflows
        └── main.yml

```
