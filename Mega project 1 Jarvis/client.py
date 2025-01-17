import google.generativeai as genai

genai.configure(api_key="Put your api key")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("I want gemini api to give short answers")
print(response.text)
