# Bubble Connector — Discovery & Vendor API Specification

**Официальный сайт:** https://bubble.io  
**Базовый эндпоинт API:** `https://<app-name>.bubbleapps.io/api/1.1`  
**Схема авторизации:** API Token (Authorization: Bearer <token>)

## Поддерживаемые сущности API
- объекты базы данных Data API (/obj/{typename})
- серверные воркфлоу Workflow API (/wf/{workflow_name})

## Архитектурные требования
- Использование безопасного клиента с контролем таймаутов, повторных попыток (backoff) и обработкой rate limit.
- Валидация входных данных через Pydantic-схемы без утечки чувствительных полей в логи.
- Тестовая точка проверки подключения: `GET /api/1.1/meta`.
