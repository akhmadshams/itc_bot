from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="data/main.db")

# text = '🐍Kundan kunga talab oshib borayotgan Python dasturlash tili haqida.\n➖Python dasturlash tiliga kundan kun talab oshib bormoqada va ko\'plab gigant kompaniyalar Google, Instagram, Youtube, Netlify Python dasturlash tilidan foydalanmoqda.\n➖Pythonning muvafaqiyat omillaridan biri sodda tuzilganligi va o\'rganish osonligi aynan dasturlashni 0 dan boshlayotganlar uchun juda to\'g\'ri tanlovdir.\n➖Python dasturchilari dasturlash sohasida eng yuqori ish haqqi to\'lanadigan mutaxasislar sirasiga kiradi.\n➖AQSHda Python dasturchilarining o\'rtacha ish haqqi 120.000$ atrofida.\n➖O\'zbekistonda ham Python dasturchilariga talab katta va kundan kunga bu talab kuchayib bormoqda.'
# await call.message.edit_reply_markup()