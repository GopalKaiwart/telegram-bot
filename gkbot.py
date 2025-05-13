import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

# Get Bot Token from Environment Variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Handle Join Request
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

# Build the Application with the provided Bot Token
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Add Handler for Join Request
app.add_handler(ChatJoinRequestHandler(approve_request))

# Start the Bot with Polling
if __name__ == "__main__":
    app.run_polling()
