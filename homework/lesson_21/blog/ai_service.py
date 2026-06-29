from google import genai
from django.conf import settings


def generate_text(prompt: str) -> str:
    if not settings.GEMINI_API_KEY:
        raise ValueError("Brak GEMINI_API_KEY w ustawieniach projektu.")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text.strip()