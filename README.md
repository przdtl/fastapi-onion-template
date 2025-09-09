# FastAPI Onion Template

Шаблон проекта на **FastAPI**, построенный по принципам **луковой архитектуры**.  
Проект разделён на слои, что упрощает поддержку, тестирование и развитие приложения.

---

## 📂 Структура проекта

```

.
├── application/       # Слой приложения (use-cases, бизнес-логика)
├── domain/            # Слой домена (сущности, интерфейсы)
├── infrastructure/    # Слой инфраструктуры (БД, репозитории, внешние сервисы)
├── presentation/      # Слой представления (FastAPI endpoints, сериализация, DI)
├── tests/             # Тесты
├── docker/            # Docker-скрипты для dev/test/prod окружений
├── pyproject.toml     # Зависимости (poetry)
└── README.md

````

### Основные слои:

- **Domain**  
  Чистый слой с бизнес-сущностями и интерфейсами (протоколами). Не зависит от внешних библиотек.

- **Application**  
  Use-case слой: сценарии работы приложения, которые используют сущности домена и абстракции.

- **Infrastructure**  
  Реализация интерфейсов (репозитории, интеграции, работа с БД, брокерами и т.д.).

- **Presentation**  
  Веб-слой: FastAPI роуты, DTO, сериализация, DI и запуск приложения.

---

## 🚀 Запуск проекта

Запуск осуществляется только через **Docker Compose**.  
В зависимости от стадии (`dev`, `test`, `prod`) используются разные `.env` файлы и разные compose-файлы.

 Примеры файлов:

- Для разработки: `.env.dev` → создаём на основе `.env.dev.example`
- Для тестов: `.env.test` → создаём на основе `.env.test.example`
- Для продакшена: `.env.prod` → создаём на основе `.env.prod.example`


### Пример для тестового окружения:

```bash
docker compose --env-file .env.test -f docker-compose.test.yml up --build
```

### Для разработки:
```bash
docker compose --env-file .env.dev -f docker-compose.dev.yml up --build
```

### Для продакшена:
```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml up --build -d
```

---

## 🧪 Тестирование

Тесты лежат в папке `tests/` и покрывают все уровни архитектуры.

Запуск:

```bash
poetry run pytest
```

или в Docker:

```bash
docker compose run --rm app pytest
```

---

## 🎯 Преимущества шаблона

* Чистая **луковая архитектура**: отделение бизнес-логики от инфраструктуры.
* Лёгкое тестирование: можно подменять реализации интерфейсов.
* Гибкая расширяемость: удобно добавлять новые слои и сервисы.
* Поддержка **Docker** и **Poetry** из коробки.
* Готовая структура для **CI/CD** и командной разработки.

---

## 📖 Полезные ссылки

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Domain-Driven Design](https://martinfowler.com/tags/domain%20driven%20design.html)
* [The Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/)

---
