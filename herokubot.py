import logging
import os
import time

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

sahamkol = "ستران ثفارس"



def start(bot, update):
    update.effective_message.reply_text("سلام.")
    time.sleep(.5)
    update.effective_message.reply_text("به پاندا خوش اومدی!")

def tahlil(bot, update):
    sahm = update.effective_message.text
    eslahy = sahm.replace('ی', 'ي')
    eslahK = eslahy.replace('ک', 'ك')
    print(eslahK)
    if eslahK in sahamkol:
    update.effective_message.reply_text("آخیششش")
    else:
    update.effective_message.reply_text("qqqq")



if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "1139770167:AAErOC1_mzcX3mOl671nu2DOTUV9ubh8V28"
    NAME = "bfoggoidfo"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, tahlil))


    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.start_polling()
    updater.idle()
