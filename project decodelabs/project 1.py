from datetime import datetime
print("=" * 60)
print(" RULE-BASED AI CHATBOT")
print(" Made by Bhaumik Bisht")
print(" Started on:", datetime.now().strftime("%d-%m-%Y"))
print(" Time:", datetime.now().strftime("%I:%M:%S %p"))
print("=" * 60)
knowledge_base = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! Hope you're having a great day.",
    "how are you": "I'm doing great! Thanks for asking.",
    "your name": "I am a Rule-Based AI Chatbot.",
    "who made you": "I was created by Bhaumik Bisht.",
    "date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}.",
    "time": f"Current time is {datetime.now().strftime('%I:%M:%S %p')}.",
    "help": """
I can respond to:
• hello / hi / hey
• how are you
• your name
• who made you
• date
• time
• thanks
• bye / exit / quit
""",
    "thanks": "You're welcome! Happy to help.",
}

chat_history = []

print("\nChatbot: Hello! Type 'help' to see available commands.")
print("Chatbot: Type 'exit', 'quit', or 'bye' to end the chat.\n")

while True:
    
    user_input = input("You: ")
    
    user_input = user_input.strip().lower()
    
    if user_input == "":
        print("Chatbot: Please enter a message.")
        continue
    
    chat_history.append(("User", user_input))
    
    if user_input in ["exit", "quit", "bye"]:
        farewell = (
            f"Goodbye! Session ended on "
            f"{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}."
        )
        print("Chatbot:", farewell)
        chat_history.append(("Bot", farewell))
        break
    
    elif user_input == "date":
        response = f"Today's date is {datetime.now().strftime('%d-%m-%Y')}."

    elif user_input == "time":
        response = f"Current time is {datetime.now().strftime('%I:%M:%S %p')}."
        
    elif user_input in knowledge_base:
        response = knowledge_base[user_input]

    else:
        response = (
            "Sorry, I don't understand that yet. "
            "Type 'help' to see available commands."
        )
        
    chat_history.append(("Bot", response))
    print("Chatbot:", response)


print("\n" + "=" * 60)
print("📜 CHAT SESSION SUMMARY")
print("=" * 60)

for speaker, message in chat_history:
    print(f"{speaker}: {message}")

print("=" * 60)
print("✅ Program terminated successfully.")
print("👨‍💻 Made by Bhaumik Bisht")
print("=" * 60)
