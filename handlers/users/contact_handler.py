from aiogram.types import Message
from loader import dp,db,bot
from keyboards.default.menu import contact, main


@dp.message_handler(text='⚙️ Xizmatlarimiz haqida')
async def contact_handler(message: Message):
    await message.answer('Tez kunda ..\nSoon ..', reply_markup=main)


@dp.message_handler(text='📝 Savol yoki taklif')
async def question(message: Message):
    await message.answer('bu yerda siz adminga habar yullashingiz mumkin ')
    # bu funksiyani uzgartiramiz baza boglaymiz bu yerga ham state bilan

@dp.message_handler(text='🎯 Biz haqimizda')
async def call_handler(message: Message):
    text = '<b>Dang\'ara IT Markazi zamonaviy kasblar akademiyasi va talabingizga mos dasturiy mahsulotlar ishlarib chiqaruvchi dasturchilardan iborat zamonaviy markaz.\n</b>'
    text += '<b>Bizning markazda 15 dan ortiq kompyuterlar va zamonaviy qurilmalar mavjud.\n\n</b>'
    text += '<b>☎️ Telefon: +998913273231\n</b>'
    text +='<b>🧑‍💻 Telegram: @akhmad_shams</b>\n'
    text +='<b>🔗 Telegram Kanal: @dangara_ITCenter</b>'
    await message.answer(text)
