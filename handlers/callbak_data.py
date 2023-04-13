import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username
import random
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

content =  -1001209009179

class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()




@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):

    if call.data == 'go_1':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Дальше⬇️', callback_data='go_2')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=24,reply_markup=markup)

    if call.data == 'go_2':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Вперёд', callback_data='go_3')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=26,reply_markup=markup)

    if call.data == 'go_3':
        change_status(call.message.chat.id)
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Конечно!', callback_data='go_4')
        markup.add(bat_a)

        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=28)
        await asyncio.sleep(2)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=30)
        await asyncio.sleep(16)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=31)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=32,reply_markup=markup)

    if call.data == 'go_4':
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text="Let's GO🔥", url = 'https://t.me/BekirSPRINTbot?start=Arbitraj_Sprint')
        markup.add(bat_a)
        await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=34,reply_markup=markup)


    try:
        await bot.answer_callback_query(call.id)
    except:
        pass
