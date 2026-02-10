# Boto_Test
Тестовое задание для Boto Education

## Как запустить проект:

1) Склонировать проект 

```bash
git clone git@github.com:vatut007/Boto_Test.git
```

2) Выполнить установку зависимостей

```bash
poetry install
```

3) Выполнить тесты

```bash
pytest
```

4) Запустить проект 

```bash
fastapi dev src/main.py
```

## Улучшения 
Для корректной работы с асинхронным FastApi можно было бы использовать асинхроную библиотеку для SQLlite, например aiosqlite
Можно было бы создать модели SQLModel, тогда не нужно было бы делать отдельные схемы апи.