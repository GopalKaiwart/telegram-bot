import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

flask_app = Flask(__name__)
tg_app = ApplicationBuilder().token(BOT_TOKEN).build()

# Handle join request
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

tg_app.add_handler(ChatJoinRequestHandler(approve_request))

@flask_app.route("/webhook", methods=["POST"])
async def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return "OK", 200

@flask_app.before_first_request
def set_webhook():
    from telegram import Bot
    bot = Bot(BOT_TOKEN)
    bot.set_webhook(f"{WEBHOOK_URL}/webhook")

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=10000)
