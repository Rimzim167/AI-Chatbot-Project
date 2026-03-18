import requests

API_KEY = "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"

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("🤖 AI Chatbot Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    data = {
        "model": "deepseek/deepseek-chat-v3",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            print("Bot:", result["choices"][0]["message"]["content"])
        else:
            print("Error:", result)

    except Exception as e:
        print("Error:", e)