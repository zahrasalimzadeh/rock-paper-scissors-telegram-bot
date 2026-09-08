import random
import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = telebot.TeleBot(TOKEN)

images = {
    "stone": "سنگ.png",
    "paper": "کاغذ.png",
    "scissors": "قیچی.png",
}

win_images = {
    "stone": "برد_سنگ.png",
    "paper": "برد_کاغذ.png",
    "scissors": "برد_قیچی.png",
}

choices_fa = {
    "stone": "🪨 سنگ",
    "paper": "📄 کاغذ",
    "scissors": "✂️ قیچی"
}

def build_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🪨 سنگ", callback_data="stone"),
        types.InlineKeyboardButton("📄 کاغذ", callback_data="paper"),
        types.InlineKeyboardButton("✂️ قیچی", callback_data="scissors"),
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "سلام! به بازی سنگ کاغذ قیچی خوش اومدی 🪨 📄 ✂️\nیکی رو انتخاب کن:",
        reply_markup=build_keyboard()
    )

@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    chat_id = call.message.chat.id
    user_choice = call.data
    bot_choice = random.choice(["stone", "paper", "scissors"])

    with open(images[user_choice], "rb") as photo:
        bot.send_photo(chat_id, photo, caption=f"شما انتخاب کردید: {choices_fa[user_choice]}")

    with open(images[bot_choice], "rb") as photo:
        bot.send_photo(chat_id, photo, caption=f"ربات انتخاب کرد: {choices_fa[bot_choice]}")

    if user_choice == bot_choice:
        winner_choice = None
        result_text = "شما برابر شدید 🤝"
    elif (user_choice == "stone" and bot_choice == "scissors") or \
        (user_choice == "paper" and bot_choice == "stone") or \
        (user_choice == "scissors" and bot_choice == "paper"):
        winner_choice = user_choice
        result_text = "تو بردی! 🎉"
    else:
        winner_choice = bot_choice
        result_text = "ربات برد! 😅"

    if winner_choice:
        with open(win_images[winner_choice], "rb") as photo:
            bot.send_photo(chat_id, photo, caption=result_text)
    else:
        bot.send_message(chat_id, result_text)

    bot.send_message(chat_id, "دوباره بازی کنیم؟ یکی رو انتخاب کن:", reply_markup=build_keyboard())

bot.polling()