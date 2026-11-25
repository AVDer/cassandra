import os
import dotenv

from openai import OpenAI

model_name = "chat"

messages = [
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Tell me a joke"}
]

dotenv.load_dotenv()

client = OpenAI(
    base_url="http://localhost:4000",
    api_key=os.getenv("LITELLM_MASTER_KEY"),
)

resp = client.chat.completions.create(
    model=model_name,
    messages=messages,
)

print(resp.choices[0].message.content)
print(resp.usage)