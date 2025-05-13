from flask import Flask, request
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatJoinRequestHandler,
)

import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

app = Flask(__name__)

telegram_app = ApplicationBuilder().token(BOT_TOKEN).build()

async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

telegram_app.add_handler(ChatJoinRequestHandler(approve_request))

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "ok"

@app.route('/')
def home():
    return "Bot is running!"

# Set the webhook
@app.before_first_request
def set_webhook():
    telegram_app.bot.set_webhook(url=WEBHOOK_URL + '/webhook')

if __name__ == '__main__':
    app.run(port=5000)
