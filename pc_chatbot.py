from gpt4all import GPT4All

model = GPT4All(r"C:\Users\Jed\AppData\Local\nomic.ai\GPT4All\gpt4all-falcon-newbpe-q4_0.gguf")

print("PC HELPER!")
print("type exit to quit")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    prompt = f"You are a professional PC technician. Help the user troubleshoot their problem in a simple and detailed way. Question: {user_input}"

    response = model.generate(prompt, max_tokens=120, temp=0.7)
    print("Bot: ", response.strip(), "\n")
    print()
