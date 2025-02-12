import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Set API Keys
GEMINI_API_KEY = "AIzaSyABWpkbbkvngB7v7tI_lDJfjFMbKcbA5fQ"
TELEGRAM_BOT_TOKEN = "7798993298:AAEe6lv2hZAvI9DcAeWfR-AWqYa-nbbVUVM"

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Function to personalize responses
def personalize_response(response_text):
    return f"My name is Kaustav. I am an AI.\n\n{response_text}"

# Handle incoming messages
async def chat_with_gemini(update: Update, context: CallbackContext):
    user_message = update.message.text
    chat = model.start_chat(history=[])
    
    try:
        response = chat.send_message(user_message)
        reply_text = personalize_response(response.text)
    except Exception as e:
        reply_text = "Sorry, an error occurred."

    await update.message.reply_text(reply_text)

# Start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("My name is Kaustav. I am an AI.\n\nHow can I assist you?")

# Main function to start the bot
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gemini))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()