# Антиспам/антимат бот для телеграм канала

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config
import re
# Импортирую свой список из регулярных выражений, которые ловят мат/спам
from anti_list import raw_list

bot = Bot(token=config.token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(content_types=['text'])
async def main(m:types.Message):
    if m['from'].is_bot:
        # Удаляем сообщение от бота
        await bot.delete_message(chat_id=m.chat.id, message_id=m.message_id)
        return
    for i in raw_list:
        if re.search(i, m.text.lower()):
            # Удаляем сообщение
            await bot.delete_message(chat_id=m.chat.id, message_id=m.message_id)
            break

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)