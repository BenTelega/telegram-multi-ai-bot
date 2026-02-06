# AGENTS.md - Guidelines for AI Coding Agents

## Project Overview
Multi-AI Telegram Bot - A Python-based Telegram bot using aiogram v3 that integrates with multiple AI models (Llama, DeepSeek, Claude, Grok) via OpenRouter API.

## Build/Run Commands

```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Run
python main.py

# Linting (install if needed)
pip install ruff black mypy
ruff check .
black --check .
mypy .

# Testing (single test - when tests are added)
pytest tests/test_specific.py::test_function -v
pytest tests/ -v
```

## Code Style Guidelines

### Imports
- Group imports: stdlib → third-party → local modules
- Separate groups with blank lines
- Use absolute imports for local modules (e.g., `from app.handlers import router`)

```python
import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers import router
```

### Formatting
- 4 spaces for indentation
- No trailing whitespace
- Max line length: 88-100 characters
- Use double quotes for strings consistently

### Types
- Use type hints for function parameters and return values
- Use `async def` for all async functions
- Return type `-> str` for model functions

```python
async def model_anthropic(text: str) -> str:
    ...
```

### Naming Conventions
- Variables/functions: `snake_case`
- Constants: `UPPER_CASE` (e.g., `SYSTEM`, `MODEL_CALLS`)
- Classes: `PascalCase`
- Modules: `snake_case.py`

### Error Handling
- Use try/except blocks for API calls
- Log errors appropriately
- Provide user-friendly error messages in Russian

```python
try:
    response = await generate(message.text)
except Exception as e:
    await message.answer(f"⚠️ Не удалось сгенерировать ответ: {e}")
```

### Project Structure
```
app/
  models/          # AI model integrations (one file per model)
  Utils/           # Utility functions (render.py for markdown)
  handlers.py      # Telegram bot handlers
  keyboards.py     # Inline keyboards
  states.py        # FSM states
  dicts.py         # Model registries and mappings
main.py            # Entry point
```

### Adding New Models
1. Create `app/models/<model_name>.py` with `async def model_<name>(text: str) -> str`
2. Add import and entry to `MODEL_CALLS` in `app/dicts.py`
3. Add title/alias to `MODEL_TITLES` in `app/dicts.py`
4. Update keyboard in `app/keyboards.py` if needed

### Environment Variables
- Load with `load_dotenv()` at module level for model files
- Use `os.getenv()` to access secrets
- Never commit `.env` files

### Async Patterns
- Use `asyncio.sleep()` for UX delays (typing indicators)
- Use `await state.set_state()` for FSM transitions
- Handle `FSMContext` properly in handlers

### Security
- Never log or expose API keys
- Use `html.escape()` when rendering user content
- Keep tokens and secrets in `.env` only

### Comments
- Use Russian for inline comments explaining logic
- Use docstrings for functions (English preferred)

## Dependencies
Core: aiogram>=3.6, openai>=1.40.0, python-dotenv>=1.0.1, httpx>=0.27.0
