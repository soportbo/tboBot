import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.process_update(update)
    return 'ok'

def start(update, context):
    update.message.reply_text("¡Hola! El bot está funcionando correctamente.")

@app.route('/')
def index():
    return 'Bot activo.'

if __name__ == '__main__':
    app.run(debug=True)
