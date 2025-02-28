from google import genai

client = genai.Client(api_key="AIzaSyC35ccVOo3abTlIkTg1g9VBFN24Ois0kPM")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)