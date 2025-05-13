from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatJoinRequestHandler

# Replace this with your actual bot token
BOT_TOKEN = "8038238607:AAFGak20SRXeQGdSig7l83Cn3qQXTWGTmos"

# Function that runs every time someone requests to join
async def approve_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    print(f"Approved: {update.chat_join_request.from_user.username}")

# Initialize the bot with the token
app = ApplicationBuilder().token(BOT_TOKEN).build()

# Tell the bot to use the 'approve_request' function for join requests
app.add_handler(ChatJoinRequestHandler(approve_request))

# Start the bot and keep it running
app.run_polling()
