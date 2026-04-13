from flask import Flask
from threading import Thread
from config import PORT

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=PORT)

def keep_alive():
    t = Thread(target=run)
    t.start()
