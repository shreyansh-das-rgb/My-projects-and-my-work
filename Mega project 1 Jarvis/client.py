import google.generativeai as genai

genai.configure(api_key="AIzaSyCKG6YFc23MhplPbSdcVuxrCrxPVjhT1zQ")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("I want gemini api to give short answers")
print(response.text)