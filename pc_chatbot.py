from gpt4all import GPT4All
import os

model = GPT4All(r"C:\Users\Jed\AppData\Local\nomic.ai\GPT4All\gpt4all-falcon-newbpe-q4_0.gguf")

def find_file(filename, search_path=r"C:\\Users\Jed"):
    for root, dirs, files in os.walk(search_path):
        if filename.lower() in (f.lower() for f in files):
            return os.path
    return "file not found"

print("Hello I'm your assisstant. How can i help?")
print("type exit to quit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    if "open" in user_input.lower():
        app_name = user_input[5:].strip()
        print("searching")

        app_path = find_file(app_name + ".exe", r"C:\Program Files")
        
        if not app_path:
            app_path = find_file(app_name + ".exe", r"C:\Program Files(x86)")

        if not app_path:
            app_path = find_file(app_name + ".exe", r"C:\Users\Jed\Desktop")
        
        if app_path:
            print(f"Bot: Found {app_name} at {app_path}")
            print("launching...")
            os.startfile(app_path)
        else:
            print("couldn't find app. try specifying the app name")
        continue



    if "find" in user_input.lower() or "where" in user_input.lower():
        filename = user_input.replace("find", "").replace("where", "").replace("is", "").strip()
        result = find_file(filename)
        print ("Bot: ", result, "\n")


    prompt = f"You are a professional PC technician or Assistant. Help the user troubleshoot their problem and assist the user in finding files and other computer related tasks in a simple and detailed way. Question: {user_input}"

    response = model.generate(prompt, max_tokens=150, temp=0.7)
    print("Bot: ", response.strip(), "\n")
    print()
