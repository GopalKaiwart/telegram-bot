from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler
import os

# Read the bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Define handler function to auto-approve join requests
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"✅ Approved: {update.chat_join_request.from_user.username}")

# Initialize the bot application
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add the join request handler
app.add_handler(ChatJoinRequestHandler(approve_request))

# Read the Render-provided port and your webhook URL
PORT = int(os.environ.get("PORT", 8443))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")  # e.g., https://your-bot-name.onrender.com/webhook

# Run the bot using webhook (not polling)
app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    webhook_url=WEBHOOK_URL
)
