import pyautogui
import pyperclip
import time
import google.generativeai as genai
import platform
import os
# Clear the clipboard on Windows
def clear_clipboard():
    if platform.system() == "Windows":
        os.system("echo off | clip")
    elif platform.system() == "Linux":
        os.system("xclip -selection clipboard /dev/null")
    elif platform.system() == "Darwin":  # macOS
        os.system("echo '' | pbcopy")
    else:
        pyperclip.copy("") 

clear_clipboard()


genai.configure(api_key="GIVE UR API KEY")
# Step 1: Click on the icon
pyautogui.click(1218,1056)
pyautogui.click(1218,1056)
pyautogui.click(1083,939)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)


pyautogui.click(704,234)
time.sleep(1)  # Ensure the click is registered

# Step 2: Drag to select text
pyautogui.moveTo(704, 234)  # Start of selection
pyautogui.mouseDown()        # Press the mouse button
pyautogui.moveTo(1775,883, duration=1)  # Drag to the end
pyautogui.mouseUp()          # Release the mouse button
time.sleep(0.5)

# Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')  # Use Ctrl+C
pyautogui.click(1775,883)
time.sleep(0.5)  # Allow clipboard to update
chat_history = pyperclip.paste()

# Step 4: Retrieve clipboard content
pyautogui.click(1218,1056)
pyautogui.click(1218,1056)
pyautogui.click(1083,939)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)
pyautogui.click(1639, 1412)


pyautogui.click(704,234)
time.sleep(1)  # Ensure the click is registered

# Step 2: Drag to select text
pyautogui.moveTo(719,369)  # Start of selection
pyautogui.mouseDown()        # Press the mouse button
pyautogui.moveTo(1775,883, duration=1)  # Drag to the end
pyautogui.mouseUp()          # Release the mouse button
time.sleep(0.5)

# Step 3: Copy the selected text
pyautogui.hotkey('ctrl', 'c')  # Use Ctrl+C
pyautogui.click(1775,883)
time.sleep(0.5)  # Allow clipboard to update
chat_history1 = pyperclip.paste()


print("Copied text:", chat_history)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"(Your role is Shreyansh Another profile here and you speak english and is a programmer.You will analyse the chat the give answer as shreyansh another profile so here is the chat) 1.[{chat_history}] (and i also forgot to tell pretend like u are shreyansh another profile and ONLY answer the chat as Shreyansh another profile no more extra comments)(and also speak only in one language)(If for some reason i havent send the chat then use this 2.[{chat_history1}] and listen if both of the chats appear then use the chat i have send u in the first one not the second one)(AND REMEMBER JUST REPLY LIKE A NORMAL HUMAN BEING)")
reply = response.text
print(reply)
pyperclip.copy(reply)


pyautogui.click(1059,955)
time.sleep(1)

pyautogui.hotkey('ctrl','v')
time.sleep(1)

pyautogui.press('enter')

pyperclip.copy("")

clear_clipboard()
