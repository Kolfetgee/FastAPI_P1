# FastAPI_P1

Учебный проект на FastAPI с реализацией слоистой архитектуры и JWT-аутентификации.

## Что реализовано

### User API
- получить одного пользователя
- получить нескольких пользователей по списку id
- получить всех пользователей
- создать одного пользователя
- создать нескольких пользователей
- обновить пользователя
- удалить пользователя

### Auth API
- регистрация пользователя
- вход пользователя
- выдача access token
- выдача refresh token
- обновление access token через refresh token
- JWT auth через dependencies
- JWT auth через middleware

## Стек
- FastAPI
- Pydantic
- pydantic-settings
- PyJWT
- pytest
- uv

## Структура проекта
```text
src/
├── apps/
│   ├── user/
│   │   ├── schemas.py
│   │   ├── services.py
│   │   ├── repository.py
│   │   └── routers.py
│   └── auth/
│       ├── schemas.py
│       ├── services.py
│       ├── connector.py
│       ├── dependencies.py
│       ├── middleware.py
│       ├── utils.py
│       └── routers.py
├── routers/
│   └── api_v1_router.py
├── settings/
│   └── settings.py
├── utils/
│   └── store.py
└── main.py
```

## Запуск проекта
```bash
uv sync
uv run uvicorn src.main:app --reload
```
## Запуск тестов
```bash
uv run pytest -v tests/test_app.py
```
## Примечание

В качестве учебной базы данных используется `Store` с доступом через контекстный менеджер.