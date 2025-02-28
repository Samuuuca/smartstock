from google import genai
import os

client = genai.Client(api_key=os.getenv("TOKEN_API_GEMINI"))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)
