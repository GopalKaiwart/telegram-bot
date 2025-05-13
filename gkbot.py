from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

app = Flask(__name__)
tg_app = ApplicationBuilder().token(BOT_TOKEN).build()

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"✅ Approved: {update.chat_join_request.from_user.username}")

tg_app.add_handler(ChatJoinRequestHandler(approve))

@app.route("/", methods=["GET", "POST"])
def index():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
async def webhook():
    if request.method == "POST":
        await tg_app.update_queue.put(Update.de_json(request.get_json(force=True), tg_app.bot))
        return "ok"

# Set webhook when app starts
async def set_webhook():
    await tg_app.bot.set_webhook(f"{WEBHOOK_URL}/webhook")

import asyncio
asyncio.run(set_webhook())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
