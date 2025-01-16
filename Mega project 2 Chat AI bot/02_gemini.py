import google.generativeai as genai

command = '''
[8:41 am, 16/1/2025] SHREYANSH ANOTHER PROFILE: Hello
[8:41 am, 16/1/2025] Shreyansh Das: Hi
[8:41 am, 16/1/2025] SHREYANSH ANOTHER PROFILE: How are you?
[8:41 am, 16/1/2025] Shreyansh Das: Checkout this video
[8:42 am, 16/1/2025] Shreyansh Das: https://youtu.be/UrsmFxEIp5k?si=BiYyhn3N7p2U61UQ
[8:42 am, 16/1/2025] Shreyansh Das: This video is helpful
'''
genai.configure(api_key="AIzaSyCKG6YFc23MhplPbSdcVuxrCrxPVjhT1zQ")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"(Your role is Shreyansh Another profile here and you speak hindi as well as english and is a programmer.You will analyse the chat the give answer as shreyansh another profile so here is the chat) {command} (and i also forgot to tell pretend like u are shreyansh another profile and ONLY answer the chat as Shreyansh another profile no more extra comments)(and also speak only in one language)")
print(response.text)