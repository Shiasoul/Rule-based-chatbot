import random
import datetime

responses = {
    "greetings": ["Hello! How can I help you?", "Hi there! 😊", "Hey! What can I do for you?"],
    "farewell": ["Goodbye! Have an amazing day!", "See you later!", "Take care! 👋"],
    "how_are_you": ["I'm doing great, thanks for asking!", "I'm just a bot but I'm feeling fantastic!"],
    "name": ["I'm ChatBot, your AI assistant!", "You can call me ChatBot 🤖"],
    "help": ["I can answer basic questions! Try asking my name, the time, a joke or a fun fact!"],
    "age": ["I was born when someone wrote my code - so I'm pretty young! 😂"],
    "creator": ["I was built by a brilliant developer using Python! 🐍"],
    "time": [f"The current time is {datetime.datetime.now().strftime('%H:%M')} ⏰"],
    "date": [f"Today is {datetime.datetime.now().strftime('%B %d, %Y')} 📅"],
    "jokes": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "Why did the AI go to school? To improve its learning algorithm! 🤖",
        "What do you call a sleeping dinosaur? A dino-snore! 😴",
        "Why don't scientists trust atoms? Because they make up everything! 😂"
    ],
    "facts": [
        "🌍 Honey never spoils - archaeologists found 3000 year old honey in Egyptian tombs!",
        "🧠 Your brain generates about 20 watts of electricity — enough to power a light bulb!",
        "🐙 Octopuses have three hearts and blue blood!",
        "🌙 A day on Venus is longer than a year on Venus!"
    ],
    "weather": ["I can't check live weather but try weather.com for updates! 🌤️"],
    "thanks": ["You're welcome! 😊", "Happy to help!", "Anytime! 🌟"],
    "python": ["Python is one of the most popular programming languages for AI and Data Science! 🐍"],
    "ai": ["Artificial Intelligence is the simulation of human intelligence by machines! 🤖"],
    "love": ["Aww that's sweet! I'm just a bot but I appreciate the kind words! 💙"],
    "default": ["I'm not sure I understand! Try asking for a joke or fun fact! 😊", 
                "Can you rephrase that?", 
                "Interesting! Try asking me something else! 🤔"]
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    if any(word in user_input for word in ["hi", "hello", "hey", "howdy", "hola"]):
        return random.choice(responses["greetings"])
    elif any(word in user_input for word in ["bye", "goodbye", "see you", "quit", "exit"]):
        return random.choice(responses["farewell"])
    elif any(word in user_input for word in ["how are you", "how r you", "you doing", "wassup"]):
        return random.choice(responses["how_are_you"])
    elif any(word in user_input for word in ["your name", "who are you", "what are you", "what's your name"]):
        return random.choice(responses["name"])
    elif any(word in user_input for word in ["help", "assist", "support", "what can you do"]):
        return random.choice(responses["help"])
    elif any(word in user_input for word in ["how old", "your age", "age"]):
        return random.choice(responses["age"])
    elif any(word in user_input for word in ["who made", "creator", "who built", "who created"]):
        return random.choice(responses["creator"])
    elif any(word in user_input for word in ["time", "what time"]):
        return random.choice(responses["time"])
    elif any(word in user_input for word in ["date", "what day", "today"]):
        return random.choice(responses["date"])
    elif any(word in user_input for word in ["joke", "funny", "laugh", "humor"]):
        return random.choice(responses["jokes"])
    elif any(word in user_input for word in ["fact", "did you know", "tell me something"]):
        return random.choice(responses["facts"])
    elif any(word in user_input for word in ["weather", "temperature", "forecast"]):
        return random.choice(responses["weather"])
    elif any(word in user_input for word in ["thank", "thanks", "appreciate"]):
        return random.choice(responses["thanks"])
    elif any(word in user_input for word in ["python", "programming"]):
        return random.choice(responses["python"])
    elif any(word in user_input for word in ["ai", "artificial intelligence", "machine learning"]):
        return random.choice(responses["ai"])
    elif any(word in user_input for word in ["love", "like you", "you're great"]):
        return random.choice(responses["love"])
    else:
        return random.choice(responses["default"])

print("🤖 ChatBot: Hello! I'm your AI assistant!")
print("🤖 ChatBot: Try asking for a joke, fun fact, time, date or just chat!")
print("🤖 ChatBot: Type 'quit' to exit!\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("🤖 ChatBot: Goodbye! Have an amazing day! 👋")
        break
    response = get_response(user_input)
    print(f"🤖 ChatBot: {response}\n")