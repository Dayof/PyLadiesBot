# -*- coding: utf-8 -*-
import sys
import time
import telepot
import configparser
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

chat_id, user_id, username = (None,None,None)
votes = { 'yes': 0, 'no': 0 }
blocked_users = []

def onChatMessage(msg):
    global user_id, chat_id, username
    
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Confirmar',
                                        callback_data='yes')],
                    [InlineKeyboardButton(text='Recusar',
                                        callback_data='no')]
                ])

    if 'new_chat_member' in msg:
        if msg['new_chat_member']['username'] != config['DEFAULT']['bot_username']:
            username = msg['new_chat_member']['username']
            user_id = msg['new_chat_member']['id']
            bot.sendMessage(chat_id,
                            'Confirmar usuária que entrou?',
                            reply_markup=keyboard)

def onCallbackQuery(msg):
    global user_id, chat_id, username, votes, blocked_users

    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query') 
    print('Callback Query:', query_id, from_id, query_data)

    if msg['from']['id'] != user_id and msg['from']['id'] not in blocked_users: 
        blocked_users.append(msg['from']['id'])
        if user_id and username: 
            if query_data == 'yes':
                votes['yes'] += 1
                bot.answerCallbackQuery(query_id, text='Status: {} voto(s) a favor e {} voto(s) contra'.format(votes['yes'], votes['no'])) 
                if votes['yes'] == 2:
                    votes = { 'yes': 0, 'no': 0 }
                    bot.answerCallbackQuery(query_id, text='Confirmada!')
                    bot.sendMessage(chat_id, 'Seja bem vinda PyLady '+ str(username) +'!')
                    user_id, username = (None, None)
                    blocked_users = []
            elif query_data == 'no':
                votes['no'] += 1
                bot.answerCallbackQuery(query_id, text='Status: {} voto(s) a favor e {} voto(s) contra'.format(votes['yes'], votes['no'])) 
                if votes['no'] == 2:
                    votes = { 'yes': 0, 'no': 0 }
                    bot.sendMessage(chat_id, 'Usuário '+ str(username) + ' sendo retirado..')
                    bot.kickChatMember(chat_id, user_id)
                    bot.answerCallbackQuery(query_id, text='Usuário '+ str(username) +' retirado.')
                    user_id, username = (None, None)
                    blocked_users = []
        else:
            bot.answerCallbackQuery(query_id, text='Usuária(o) já aprovada(o) ou retirada(o).')
    elif msg['from']['id'] in blocked_users:
        bot.answerCallbackQuery(query_id, text='{}, seu voto já foi contabilizado'.format(msg['from']['username']))
    else:
        bot.answerCallbackQuery(query_id, text='Aguarde aprovação do grupo.')


# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

bot = telepot.Bot(config['DEFAULT']['token'])

bot.setWebhook()

bot.message_loop({'chat': onChatMessage,
                'callback_query': onCallbackQuery},
                run_forever='Listening ...')
