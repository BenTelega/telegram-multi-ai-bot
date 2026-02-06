import os

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("AI_TOKEN"),
)

SYSTEM = (
    "Отвечай кратко и по делу. Максимум 3500 символов. "
    "Используй маркированные пункты, избегай воды. "
    "Жирным выделяй только ключевые фразы."
)


async def model_qwen(text: str) -> str:
    completion = await client.chat.completions.create(
        model="qwen/qwen3-coder:free",
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text},
        ],
        max_tokens=900,
        temperature=0,
    )
    print(completion)
    return completion.choices[0].message.content
