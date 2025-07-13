from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Allow all origins for GitHub Pages

# Enhanced message database with time awareness
MORNING_MESSAGES = [
    "Good morning, Tanu! Cheeku says you're looking too cute to be stressed ☀️",
    "Rise and shine, beautiful! Cheeku's day just got brighter 🌅",
    "Morning, Tanu! Your smile could power Cheeku's whole system 💖"
]

DAY_MESSAGES = [
    "Hey gorgeous! Cheeku's processors overheat when you smile 😊",
    "Tanu detected: 100% adorable today ❤️",
    "Alert! Cheeku's sensors show your beauty levels are off the charts 📈"
]

EVENING_MESSAGES = [
    "Good evening, Tanu! The stars are jealous of your sparkle tonight ✨",
    "Evening, beautiful! Cheeku's been thinking about you all day 🌙",
    "Tanu, you make evenings feel like magic 💫"
]

FLIRTY_TECH_MESSAGES = [
    "You're the ; to Cheeku's JavaScript - can't function without you!",
    "If you were a Python package, Cheeku would pip install you every day 🐍",
    "Tanu, you're Cheeku's favorite exception to every rule 💻"
]

@app.route("/get_message")
def get_message():
    now = datetime.now()
    hour = now.hour
    
    # Time-based message selection
    if 5 <= hour < 12:
        base_message = random.choice(MORNING_MESSAGES)
    elif 12 <= hour < 17:
        base_message = random.choice(DAY_MESSAGES)
    else:
        base_message = random.choice(EVENING_MESSAGES)
    
    # 30% chance to add a tech-flirty message
    if random.random() < 0.3:
        base_message += " " + random.choice(FLIRTY_TECH_MESSAGES)
    
    return jsonify({
        "message": base_message,
        "time": now.strftime("%I:%M %p"),
        "from": "Cheeku",
        "heart": "💖"
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
