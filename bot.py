import telebot
from telebot import types

TOKEN = "8643797404:AAFkgm6LyUlk8eIWa9ewEWe9FIVLKdLVtVU"

bot = telebot.TeleBot(TOKEN)

CHANNEL = "@RISHTON_24"

# Kino kodlari
movies = {
    "101": "https://t.me/orgimchakodam_2026/1"
}

# /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "📢 Obuna bo'lish",
        url="https://t.me/RISHTON_24"
    )

    btn2 = types.InlineKeyboardButton(
        "✅ Tekshirish",
        callback_data="check_sub"
    )

    markup.add(btn1)
    markup.add(btn2)

    bot.send_message(
        message.chat.id,
        "📢 Avval @RISHTON_24 kanaliga obuna bo'ling!\n\nObuna bo'lgach '✅ Tekshirish' tugmasini bosing.",
        reply_markup=markup
    )

# Obunani tekshirish
@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub(call):
    member = bot.get_chat_member(CHANNEL, call.from_user.id)

    if member.status in ["member", "administrator", "creator"]:
        bot.edit_message_text(
            "✅ Obuna tasdiqlandi!\n\n🎬 Endi kino kodini yuboring.",
            call.message.chat.id,
            call.message.message_id
        )
    else:
        bot.answer_callback_query(
            call.id,
            "❌ Avval @RISHTON_24 kanaliga obuna bo'ling!",
            show_alert=True
        )

# Kino kodi
@bot.message_handler(func=lambda message: True)
def kino(message):
    code = message.text.strip()

    if code in movies:
        bot.send_message(message.chat.id, f"🎬 Kino:\n{movies[code]}")
    else:
        bot.send_message(message.chat.id, "❌ Bunday kod topilmadi.")

bot.infinity_polling()