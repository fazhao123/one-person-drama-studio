"""Quick API connectivity test — verify DeepSeek works before launching app."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")

if not api_key:
    print("[FAIL] DEEPSEEK_API_KEY not set in .env")
    exit(1)

print(f"Base URL: {base_url}")

client = OpenAI(api_key=api_key, base_url=base_url)

try:
    r = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "回复一个字：好"}],
        max_tokens=5,
    )
    print(f"[OK] API works: {r.choices[0].message.content}")
except Exception as e:
    print(f"[FAIL] API Error: {e}")
