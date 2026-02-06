from app.models.llama import model_llama
from app.models.anthropic import model_anthropic
from app.models.mistral import model_mistral

MODEL_CALLS = {
    "llama": model_llama,
    "anthropic": model_anthropic,
    "mistral": model_mistral,
}

MODEL_TITLES = {
    "llama": ("Meta Llama 3.1-70B", "Llama"),
    "anthropic": ("Claude-3.5 Sonnet", "Claude"),
    "mistral": ("Mistral Small 3.1", "Mistral"),
}

INTRO_PROMPT_TEMPLATE = (
    "Сделай короткую самопрезентацию **от первого лица** для модели {title} "
    "(обращаться можно как {alias}). Структура: "
    "1–2 строки приветствия; затем маркированный список '•' из 3–5 возможностей; "
    "закончить фразой 'Чем могу помочь? 😊'. Пиши по-русски, до 500 символов, без воды. "
    "Ключевые слова выделяй **жирным**. Не упоминай токены/лимиты."
)
