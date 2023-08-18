from aiogram.types import Message, CallbackQuery, InputFile
from loader import dp, db,bot
from keyboards.inline.courses import courses_in_key
import logging

# 1 telegram server saqlash
# 2 local server saqlash
# 3 rasmdi url orqali

# 1.1 4 xil kurinishda saqlanadi
# 1.1.1 hira
# 1.1.2 hiraroq
# 1.1.3 sifatliroq
# 1.1.4 sifatli

@dp.message_handler(content_types='photo')
async def get_id(message: Message):
    file_id = message.photo[-1].file_id
    print(file_id)
    await message.reply(file_id)



# @dp.message_handler(content_types='video')
# async def video(message: Message):
#     file_id = message.video.file_id
#     await message.answer(file_id)


# @dp.message_handler(text='video')
# async def send_video(message: Message):
#     file_id = 'BAACAgIAAxkBAAII2WQ_7Ea8WCS6sosQuUsu7fsEzKeCAAJJLQACmK8AAUrogBNP7vCE8C8E'
#     chat_id = message.from_user.id
#     await bot.send_video(chat_id=chat_id, video=file_id)
#
# @dp.message_handler(text='android')
# async def send_phot(message: Message):
#     chat_id = message.from_user.id
#     file_id = 'AgACAgIAAxkBAAIISmQ_3nOCDh2eSBlCyphhyjHNzFYQAAKjxjEbmK8AAUrgj2NS5nVuPQEAAwIAA3gAAy8E'
#     text = 'rasm uchun caption'
#     await bot.send_photo(chat_id=chat_id, photo=file_id, caption=text)
#
#
# @dp.message_handler(text='python')
# async def send_py(message: Message):
#     chat_id = message.from_user.id
#     file = InputFile('media/python.jpg')
#     text = 'python uchun caption'
#     await bot.send_photo(chat_id=chat_id, photo=file, caption=text)



@dp.message_handler(text='🧾 Kurslar haqida')
async def course(message: Message):
    await message.answer('<b>Quyida yo\'nalishlar haqida ma\'lumot olishingiz mumkin 👇</b>\n\n', reply_markup=courses_in_key)


@dp.callback_query_handler(text='python')
async def python(call: CallbackQuery):

    file_id = 'AgACAgIAAxkBAAIIY2Q_4KpaJaCs5ZHIqTz3wdu1XkrKAAKhxjEbmK8AAUrqpb7L0OsujAEAAwIAA3kAAy8E'
    chat_id = call.from_user.id
    text = '🐍Kundan kunga talab oshib borayotgan Python dasturlash tili haqida.\n➖Python dasturlash tiliga kundan kun talab oshib bormoqada va ko\'plab gigant kompaniyalar Google, Instagram, Youtube, Netlify Python dasturlash tilidan foydalanmoqda.\n➖Pythonning muvafaqiyat omillaridan biri sodda tuzilganligi va o\'rganish osonligi aynan dasturlashni 0 dan boshlayotganlar uchun juda to\'g\'ri tanlovdir.\n➖Python dasturchilari dasturlash sohasida eng yuqori ish haqqi to\'lanadigan mutaxasislar sirasiga kiradi.\n➖AQSHda Python dasturchilarining o\'rtacha ish haqqi 120.000$ atrofida.\n➖O\'zbekistonda ham Python dasturchilariga talab katta va kundan kunga bu talab kuchayib bormoqda.'
    await call.answer('Python dasturlash kursi')
    # await call.message.answer('python')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat_id, photo=file_id, caption=text, reply_markup=courses_in_key)



@dp.callback_query_handler(text='android')
async def android(call: CallbackQuery):
    chat_id = call.from_user.id
    file_id = 'AgACAgIAAxkBAAIIh2Q_4zRBAAGTaZieK2Joa23ID1Z5aAACFscxG5ivAAFKvF9-nnfbFCoBAAMCAAN4AAMvBA'
    text = '👨🏻‍💻 Dunyodagi eng ommabop Mobile OS\'ga ilovalar yaratishni, o\'z ilovalaringizni dunyoning 72% smartfonlarida bo\'lishini xohlaysizmi? Unday bo\'lsa Android development kursimiz aynan siz uchun!\n\n⚡️ Kursda tajribali mentorlar tomonidan dasturchilar uchun eng muhim bilimlar:\n\n• Java va Kotlin dasturlash tillari\n• Android studio tools• Mobile interface qurish• Theme and style\'lar bilan ishlash\n• Android architect component MVVM, MVP, MVC\n• Threading (paralell tasklar bajarish)• Git bilan ishlash\n• Local database\n• Networking (retrofit, okhttp...)\n• Work manager, Navigation\n• Dependency injection\'lar Dagger2, Koin, Hilt o\'rgatiladi va har bir o\'quvchi ikkita real loyiha bilan kursni bitiradi.\n\n😎 Bunday imkoniyatni qo\'ldan boy bermang. Dasturchilik aynan shu yerdan boshlanadi!'
    await call.answer('Android Dasturlash')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat_id, photo=file_id, caption=text, reply_markup=courses_in_key)




@dp.callback_query_handler(text='backend')
async def backend(call: CallbackQuery):
    chat_id = call.from_user.id
    file_id = 'AgACAgIAAxkBAAIIkGQ_5CuqmYU2XapKfwKRd0giV67rAAJAxzEbmK8AAUpniw0SMlu-zAEAAwIAA3kAAy8E'
    text = '⚡️ Python Backend kursiga ro\'yxatdan o\'ting✅ \nDasturlashda sohani pul uchun o\'rganganlar emas, sohani haqiqatdan <b>jinnisi</b> bo\'lganlargina qadrlanadi\n\n🎯 Python, Django kurslarimizga qabul boshlanmoqda, oldindan ro\'yxatdan o\'tib o\'z joyingizni band etib qo\'yishingiz mumkin😊\n\n🔥 Haftada 3 marta 2 soatdan 6 oy davomida Python basic, Python OOP, Django, DRF, MySQL, Docker, Redis kabi texnologik ko\'nikmalarni real proyektlar va xalqaro kompaniyalar talabi darajasida o\'rganasiz.'
    await call.answer('BackEnd Kursi')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat_id, photo=file_id, caption=text, reply_markup=courses_in_key)


@dp.callback_query_handler(text='frontend')
async def frontend(call: CallbackQuery):
    chat_id = call.from_user.id
    file_id='AgACAgIAAxkBAAIIp2Q_6SFaOubL_GWgyuyqgCJSTTWkAAJRxzEbmK8AAUr9rViEx5rHkgEAAwIAA3kAAy8E'
    text = 'Dasturlashning Frontend yo\'nalishini munosib joyda, qisqa muddatda va uncha qimmat bo\'lmagan narxda o\'rganish uchun biz siz uchun eng to\'g\'ri tanlovmiz.\n✅ Hozirda Frontend yo\'nalishi bo\'yicha yangi guruh ochilayotgan bo\'lib, bu kursda siz :\n🔹Html\n🔹CSS\n🔹SASS\n🔹Figma\n🔹Java Script\n🔹Chuqurlashtirilgan Java Script\n🔹React JS va 20 dan ortiq murakkab dasturlarni noldan boshlab o\'rganasiz.'
    await call.answer('FrontEnd')
    await call.message.edit_reply_markup()
    await bot.send_photo(caption=text, chat_id=chat_id, photo=file_id, reply_markup=courses_in_key)


@dp.callback_query_handler(text='smm')
async def smm(call: CallbackQuery):
    chat_id = call.from_user.id
    file_id = 'AgACAgIAAxkBAAIIumQ_6g-ah1KtfEQ3_Tq2Gl4NR8_gAAJbxzEbmK8AAUqrN8i2qtc2AgEAAwIAA3kAAy8E'
    text = '🔖 SMM atamasi Social Media Marketing so‘zlarining bosh harflaridan tashkil topgan. Bu soha har qanday ijtimoiy tarmoqlarda sayt, mahsulot yoki xizmatni ommalashtirishga qaratilgan harakatlardir.\nSMM yordamida hal qilish mumkin bo‘lgan vazifalar:\n📌 Brend yaratish va uni yurgizish/tanitish;\n📌 Brendni mashhur qilish, unga bo‘lgan qiziqishni oshirish;\n📌 Kompaniya saytiga tashrif buyuruvchilar sonini oshirish;\n📌 Mijozlar, foydalanuvchilarda xizmat, tovar va mahsulot yuzasidan paydo bo‘lgan savollarga tezkor javob berish, xizmat ko‘rsatish.'
    await call.answer('SMM Kursi')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat_id, photo=file_id, caption=text, reply_markup=courses_in_key)



@dp.callback_query_handler(text='dizayn')
async def dizayn(call: CallbackQuery):
    chat=call.from_user.id
    file="AgACAgIAAxkBAAIImGQ_5ZHrqJz5n9gqJ5yahgLkeRhtAAJHxzEbmK8AAUrHSWZOHZyl9AEAAwIAA3gAAy8E"
    text='Grafik dizayn — dizayn sohasining yoʻnalishlaridan biri boʻlib,\n maʼlum axborotni ijtimoiy guruhlarga yetkazish uchun vizual kontent yaratish, ularni tartiblash, \nloyihalashga xizmat qiladi. Grafik dizaynning asosiy maqsadi muammolarni aniqlash va ularni ijodkorlik bilan innovatsion va \nraqamli vositalar yordamida oʻzgartirish va toʻgʻri talqin qilishdan iborat.'
    await call.answer('Grafik Dizayn Kursi')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat,photo=file,caption=text,reply_markup=courses_in_key)


@dp.callback_query_handler(text='foundation')
async def foundation(call: CallbackQuery):
    chat = call.from_user.id
    file = "AgACAgIAAxkBAAIw-GTf9qzB351nvkFw4qu-axzB3NExAAJR1TEbOdNoS9IrjsB0lm2SAQADAgADeQADMAQ"
    text = 'Asosiy Tamoyillar: Dasturlashning asosiy tamoyillarini o\'rganish, ma''lumotlarni dastur bajarish uchun qanday qilib tuzish va bajarishni tushunishga yordam beradi.\n' \
           'Dasturlash Tillari: Kursda odatda bir nechta asosiy dasturlash tili o\'qitiladi, masalan, Python, Java, C++ kabi. Bu tillar to\'g\'ridan-to\'g\'ri dasturlashni o\rganish uchun eng asosiy vosita bo\'ladi.\n' \
           'Algoritmlar va Strukturalar: Algoritmlarni tuzish, ro\'yxatlar, massivlar, tuzilgan ma\'lumotlar, grafiklar va boshqa dasturlashda kerak bo\'lgan konseptlarni o\'rganish imkonini beradi.\n' \
           'Dastur Ishlatish va Buglar Tuzatish: Dasturlarni ishlatish va ularda chiqadigan qator buglarni tuzatishni tushunishga yordam beradi.\n' \
           'Dastur Yozish Asoslari: Kurslar o\'rganuvchilarining dasturlarni yozish va tahrirlash uchun ma\'lumot olish va ularga qanday yordam bera olishi haqida ko\'rsatib beradi.'
    await call.answer('Foundation')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat, photo=file, caption=text, reply_markup=courses_in_key)



@dp.callback_query_handler(text='computer')
async def computer(call: CallbackQuery):
    chat = call.from_user.id
    file = "AgACAgIAAxkBAAIxBGTf-5iQ08AdvMun73TA8C5Xlw_bAAKxvTEbUXfhS3lT1uVOEeOVAQADAgADeQADMAQ"
    text = '👨🏻‍💻Kompyuterdan foydalanishni o\'rganish istagidamisiz?\n' \
           'U holda, bu istakni amalga oshirish vaqti keldi!\n' \
           'Dang\'ara ITCenter markazining Kompyuter savodxonligi kursida ta\'lim olish orqali siz kompyuterdan professiona tarzda foydalanish, tezkorlik bilan amallarni bajarish va yana ko\'plab boshqa bilimlarga ega bo\'lishingiz mumkin.' \

    await call.answer('Kompyuter savodxonligi')
    await call.message.edit_reply_markup()
    await bot.send_photo(chat_id=chat, photo=file, caption=text, reply_markup=courses_in_key)