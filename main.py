# -*- coding: utf-8 -*-
import sys
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '293519004:AAFFhIBJrrxYzVs9clx9g2tDpWIi84ZSiio'

def onChatMessage(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Confirmar',
                                        callback_data='yes')],
                    [InlineKeyboardButton(text='Recusar',
                                        callback_data='no')]
                ])

    bot.sendMessage(chat_id,
                    'Confirmar usuário que entrou?',
                    reply_markup=keyboard)

def onCallbackQuery(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print 'Callback Query:', query_id, from_id, query_data

    if query_data == 'yes':
        bot.answerCallbackQuery(query_id, text='Confirmado!')
    else:
        bot.answerCallbackQuery(query_id, text='Usuário retirado.')

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': onChatMessage,
                'callback_query': onCallbackQuery},
                run_forever='Listening ...')
