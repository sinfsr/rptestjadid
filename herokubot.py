import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters



if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1139770167:AAErOC1_mzcX3mOl671nu2DOTUV9ubh8V28"
    NAME = "wrvrrwvwrvwr"



    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)


dp = updater.dispatcher

#####
def start(bot, update):
    chat_id = update['message']['chat']['id']
    bot.sendMessage(chat_id, 'سلام'  + (update['message']['chat']['first_name'] ) +    ' 🐼')
    time.sleep(2)
    bot.sendMessage(chat_id,'ربات پاندا به شما خوش آمد میگه. من یه رباتم که تو هر لحظه مشغول تحلیل و بررسی سهماست ،، من نمیخوابم ، غذا نمیخورم ، و حتی گوشی هم ندارم !')
    time.sleep(.5)
    bot.sendMessage(chat_id, 'میخوای امتحان کنی؟')
    time.sleep(2)
    bot.sendMessage(chat_id, 'یه نماد بگو!')

dp.add_handler(CommandHandler('start' , start ))

#######




updater.start_polling()
updater.idle()