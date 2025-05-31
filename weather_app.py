from flask import Flask, request, jsonify, render_template
import requests
import re
import os

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")

def extract_city(message):
    match = re.search(r'weather in ([a-zA-Z ]+)', message.lower())
    return match.group(1).strip() if match else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    city = extract_city(user_msg)

    if city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url).json()

        if response.get('cod') != 200:
            return jsonify({'reply': f"Sorry, I couldn't find weather info for {city}."})

        temp = response['main']['temp']
        desc = response['weather'][0]['description'].capitalize()
        reply = f"The weather in {city.title()} is {desc} with a temperature of {temp}°C."
    else:
        reply = "Please ask about the weather in a specific city, like: 'What's the weather in London?'"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
