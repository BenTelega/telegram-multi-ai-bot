# Multi-AI Telegram Bot

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![aiogram](https://img.shields.io/badge/aiogram-v3-informational)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-success)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

Multi-AI Telegram Bot — хаб ИИ-ассистентов в Telegram с выбором модели через OpenRouter API. Поддерживает Llama, Claude и Mistral. Каждая модель имеет собственное приветствие и позиционирование.

## Ключевые возможности

- **Выбор модели при старте** с мгновенным переключением «Back to Models»
- **FSM-логика**: `choosing_model → waiting_prompt → generating`
- **Асинхронность** и anti-flood защита
- **HTML-рендер Markdown** с разбиением длинных ответов
- **Кастомные интро** под каждую модель
- **Модульная структура** — добавление новой модели за минуты
- **Docker-готовность**

## Установка

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Настройка

1. Скопируйте пример окружения:
```bash
cp .env.example .env
```

2. Заполните `.env`:
```env
TG_TOKEN=your_telegram_bot_token
AI_TOKEN=your_openrouter_api_key
```

## Запуск

```bash
python main.py
```

## Команды

- `/start` — начать и выбрать модель
- `/models` — вернуться к выбору модели
- `/cancel` — сбросить состояние

## Архитектура

```
app/
├── models/          # Интеграции с AI-провайдерами
│   ├── llama.py
│   ├── anthropic.py
│   └── mistral.py
├── handlers.py      # Telegram-обработчики и FSM
├── keyboards.py     # Inline-клавиатуры
├── states.py        # FSM-состояния
├── dicts.py         # Реестры моделей и шаблоны
└── Utils/
    └── render.py    # Markdown → HTML конвертация
main.py              # Entry point
```

## Добавление новой модели

1. Создайте `app/models/<name>.py`:
```python
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

async def model_<name>(text: str) -> str:
    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("AI_TOKEN"),
    )
    response = await client.chat.completions.create(
        model="provider/model-name",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content
```

2. Добавьте в `app/dicts.py`:
```python
from app.models.<name> import model_<name>

MODEL_CALLS = {
    ...
    "<name>": model_<name>,
}

MODEL_TITLES = {
    ...
    "<name>": ("Model Title", "Alias"),
}
```

3. Обновите `app/keyboards.py` при необходимости.

## Docker

```bash
docker-compose up -d
```

## Лицензия

MIT
