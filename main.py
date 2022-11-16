from logging import getLogger
from telegram import Bot
from telegram import Updater
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.utils.request import Request
from archive_bot.db import init_db
from archive_bot.db import add_message
from archive_bot.db import count_message
from archive_bot.db import list_message

from echo.config import load_config
from echo.utils import debug_requests

config = load_config()

logger = getLogger(__name__)

@debug_requests
def  massage_handler(update: Update, context: CallbackContext):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'аноним'
    text = update.effective_message.text
    reply_text = f'Привет, {name}!\n\n{text}'

    update.message.reply_text(
        text=reply_text,
    )


#ЗАПИСЬ СМС В БД
    if text:
        add_message(
            user_id=user,id,
            text=text,
        )

@debug_requests
def callback_handler(update: Update,contex: CallbackContext):
    user = update.effective_user
    callback_data = update.callback_query.data

    if callback_data == COMMAND_COUNT:
        count = count_messages(user_id=user.id)
        text = f'У вас {cout} сообщение!'
    elif callback_data == COMMAND_LIST:
        messages = list_message(user_id=user.id , limit=5)
        text = '\n\n'.join([f'#(message_id)'])




