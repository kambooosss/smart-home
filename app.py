

from Adafruit_IO import Client
aio = Client('kambooosss','aio_WkTo23efJXHilxBhrox8jtBNTbOj')







from telegram.ext import Updater, MessageHandler, Filters




def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on')
  aio.send('light',1)
  
def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off')
  aio.send('light',900)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="on":
    demo1(bot,update)
  elif a =="off":
    demo2(bot,update)


bot_token = '1959189837:AAHYhYl4nvq7vXGFtVWoP7ZgQWY0wB_VTtc'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle() 




