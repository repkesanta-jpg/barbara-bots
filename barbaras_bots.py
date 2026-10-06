import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("KĻŪDA: Nav BOT_TOKEN")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👗 Katalogs")
    btn2 = types.KeyboardButton("💰 Cenas un izmēri")
    btn3 = types.KeyboardButton("🛒 Pasūtīt")
    btn4 = types.KeyboardButton("🤖 Jautāt AI")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    bot.send_message(message.chat.id, f"Čau, {message.from_user.first_name}! 🌙\n\nEsmu Barbaras ceha bots! Palīdzēšu atrast kleitu.", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "👗 Katalogs")
def catalog(message):
    bot.send_message(message.chat.id, "Mūsu katalogs:\n1. Melna vakarkleita - 45 EUR\n2. Bēša vasaras kleita - 35 EUR\n3. Uzvalks - 60 EUR")

@bot.message_handler(func=lambda m: m.text == "💰 Cenas un izmēri")
def prices(message):
    bot.send_message(message.chat.id, "Izmēri: XS, S, M, L, XL\nCenas no 25-65 EUR")

@bot.message_handler(func=lambda m: m.text == "🛒 Pasūtīt")
def order(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Rakstīt Barbarai", url="https://t.me/sambellaaaaa")
    markup.add(btn)
    bot.send_message(message.chat.id, "Lai pasūtītu, spied pogu:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "🤖 Jautāt AI")
def ai_q(message):
    bot.send_message(message.chat.id, "Uzdod jautājumu - piemēram 'gribu kleitu uz kāzām'")

@bot.message_handler(func=lambda m: True)
def chat(message):
    text = message.text.lower()
    if "kāzas" in text:
        bot.send_message(message.chat.id, "Uz kāzām iesaku melno vakarkleitu - eleganta! Ir M un L.")
    elif "melna" in text:
        bot.send_message(message.chat.id, "Melna kleita S, M, L - 45 EUR.")
    elif "cena" in text:
        bot.send_message(message.chat.id, "Cenas no 25-65 EUR. Kura interesē?")
    else:
        bot.send_message(message.chat.id, f"Tu rakstīji: '{message.text}' - drīz atbildēšu gudrāk! Spied Katalogs 👗")

print("Bots startēts...")
bot.infinity_polling()
