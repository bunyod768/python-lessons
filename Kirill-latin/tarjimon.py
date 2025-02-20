from transliterate import to_cyrillic , to_latin
import telebot
token = '7215605504:AAGBjsf2gDQn50aIwfTp38oc7fYRWrURHgc'
bot = telebot.TeleBot(token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = "Assalomu alaykum!Xush kelibsiz."
	javob += "\n Matn kiriting."
	bot.reply_to(message,javob)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text   
    if msg.isascii():
       result = to_cyrillic(msg)
    else:
         result = to_latin(msg)    
    bot.reply_to(message, result )	
    
bot.infinity_polling()    

# matn = input("matn kiriting:")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
