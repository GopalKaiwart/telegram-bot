import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(approve_request))

if __name__ == "__main__":
    app.run_polling()
