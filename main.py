import sys
import time
import telepot

TOKEN = '293519004:AAFFhIBJrrxYzVs9clx9g2tDpWIi84ZSiio'

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id

    if content_type == 'text':
        bot.sendMessage(chat_id, msg['text'])

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print 'Listening ...'

while 1:
    time.sleep(10)
