# Telegra Bot

A simple Telegram bot that sends the content of `text.txt` **line by line**.

---

## Setup and Run

### 1. Create a virtual environment
```
python -m venv venv
```

### 2. Activate the virtual environment

- **On Windows (PowerShell)**:
```
venv\Scripts\activate
```

- **On Windows (Command Prompt)**:
```
venv\Scripts\activate.bat
```

- **On macOS/Linux**:
```
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create a `.env` file with your bot token
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 5. Add your text
Add the text you want to send in `text.txt` (each line will be sent separately).

### 6. Run the bot
```
python bot.py
```

### 7. Stop the bot
Press `Ctrl + C` in the terminal.

---

## Usage in Telegram

- Send `/start` to the bot to see the welcome message.
- Send `/show` to receive the text from `text.txt` **line by line**.