# AI Study Assistant

## Project Description

AI Study Assistant is a command-line Python application designed to help students manage and search study notes efficiently.

The assistant supports:
- note searching
- mathematical calculations
- note creation
- conversation memory
- command help system

The project was built using a modular Python architecture.

---

## Features

### Search Notes
Search for keywords inside the notes database.

Example:
search python

### Calculate Expressions
Perform mathematical calculations safely.

Example:
calculate 8*8

### Add Notes
Add new study notes dynamically.

Example:
add note Python is used for automation

### Conversation Memory
Store and display conversation history during runtime.

### Help Command
Display all available commands.

### Exit Command
Close the assistant safely.

---

## Project Structure

```text
ai-study-assistant/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── tools.py
│   ├── memory.py
│   └── utils.py
│
├── data/
│   ├── notes.txt
│   └── memory.txt
│
├── docs/
│   └── journal.md
│
├── tests/
│   ├── test_agent.py
│   └── test_tools.py
│
├── requirements.txt
├── README.md
└── report.md