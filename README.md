

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=24&pause=1000&color=00F2FE&center=true&vCenter=true&width=600&lines=Hi+there!+I'm+SmartBot+%F0%9F%A4%96;Rule-Based+AI+Chatbot+System;Intelligent+Pattern+Matching+%26+Responses;Automated+Conversational+Workflows" alt="Typing SVG" />
  </a>
</p>
# 🤖 Rule-Based AI Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Project](https://img.shields.io/badge/Project-AI%20Chatbot-orange)

A simple **Rule-Based AI Chatbot** developed in **Python** using conditional logic and a predefined knowledge base. The chatbot responds to user queries, provides the current date and time, maintains chat history, and displays a session summary before exiting.

---

# 📌 Project Information

| **Project Name** | Rule-Based AI Chatbot |
|------------------|-----------------------|
| **Developer** | Bhaumik Bisht |
| **Language** | Python 3 |
| **Project Type** | Artificial Intelligence (Rule-Based System) |
| **Difficulty** | Beginner |
| **Interface** | Command Line Interface (CLI) |

---

# 📖 Project Overview

This project demonstrates the fundamentals of **Artificial Intelligence using rule-based systems**. Instead of machine learning, the chatbot relies on predefined responses stored in a knowledge base (dictionary).

It interacts with users through the terminal, understands simple commands, records conversations, and displays a complete chat history when the session ends.

---

# ✨ Features

- 👋 Greets the user
- 💬 Responds to common questions
- 📅 Displays current date
- ⏰ Displays current time
- 📜 Maintains complete chat history
- 📝 Displays session summary
- ❌ Gracefully exits the program
- 🛡 Handles invalid or empty input
- 📚 Built using Python Dictionary (Knowledge Base)

---

# 🛠 Technologies Used

- Python 3
- datetime Module
- Dictionary Data Structure
- While Loop
- Conditional Statements
- String Handling

---

# 📂 Project Structure

```text
                    Rule-Based-AI-Chatbot
                              │
                              ▼
                    chatbot.py (Main Program)
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
 Project Header        Knowledge Base        Chat History
 (Title, Date, Time)   (Predefined Replies) (Stores Chat)

                              │
                              ▼
                      User Input (CLI)
                              │
                              ▼
                  Input Processing & Validation
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
         Command Found?                  Invalid Input
               │                             │
          Yes  ▼                             ▼ No
      Fetch Response               Show Help Message
               │                             │
               └──────────────┬──────────────┘
                              ▼
                    Display Chatbot Response
                              │
                              ▼
                   Save Conversation History
                              │
                              ▼
                     Exit Command Received?
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                    No              Yes
                     │                 │
                     └──────► Display Chat Summary
                                      │
                                      ▼
                             Program Terminated
```



---

# 🚀 How to Run

### Step 1

Install Python 3 from

https://www.python.org/downloads/

### Step 2

Download or clone this repository

```bash
git clone https://github.com/yourusername/Rule-Based-AI-Chatbot.git
```

### Step 3

Open Terminal or Command Prompt

Navigate to the project folder.

```bash
cd Rule-Based-AI-Chatbot
```

### Step 4

Run the program

```bash
python chatbot.py
```

---

# 💬 Available Commands

| User Input | Chatbot Response |
|------------|-----------------|
| hello | Greeting |
| hi | Greeting |
| hey | Greeting |
| how are you | Current status |
| your name | Bot introduction |
| who made you | Developer information |
| date | Shows today's date |
| time | Shows current time |
| help | Displays available commands |
| thanks | Thank you response |
| bye | Exit chatbot |
| quit | Exit chatbot |
| exit | Exit chatbot |

---

# 🖥 Sample Output

```
============================================================
RULE-BASED AI CHATBOT
Made by Bhaumik Bisht
Started on: 22-07-2026
Time: 08:45:15 PM
============================================================

Chatbot: Hello! Type 'help' to see available commands.

You: hello
Chatbot: Hello! How can I assist you today?

You: date
Chatbot: Today's date is 22-07-2026.

You: bye
Chatbot: Goodbye! Session ended successfully.
```

---

# 🧠 How It Works

1. Program starts and displays project details.
2. User enters a command.
3. Input is converted to lowercase.
4. Chatbot searches the command inside the knowledge base.
5. If found, it returns the predefined response.
6. If not found, it asks the user to type **help**.
7. Every conversation is stored in chat history.
8. On exit, the complete session summary is displayed.

---

# 📸 Screenshots
<img width="1917" height="987" alt="Screenshot 2026-07-24 144119" src="https://github.com/user-attachments/assets/aef9b050-11c9-40ad-b37a-abaa6f79db29" />



# 🎯 Learning Outcomes

This project helps understand:

- Rule-Based Artificial Intelligence
- Dictionaries in Python
- User Input Handling
- While Loops
- Conditional Statements
- String Processing
- Basic Chatbot Development
- Chat History Management

---

# 📈 Future Improvements

- Add calculator functionality
- Add jokes and fun facts
- Weather information
- GUI using Tkinter
- Voice assistant support
- Text-to-Speech
- Speech Recognition
- AI integration using APIs
- Save chat history to a text file
- Multiple chatbot personalities

--


# 👨‍💻 Developer

**Bhaumik Bisht**

Python Developer | AI Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## ⭐ Show Your Support

If you like this project,

⭐ Star this repository

🍴 Fork it

💻 Learn from it

🚀 Build something even better!
