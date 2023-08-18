import datetime

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.menu import main
from keyboards.default.menu import cancel_key, phone_key, regions_key, free_day, free_time, yunalish, addition
from states.regiter_state import RegisterState
from loader import dp, db, bot
from aiogram.types import Message, CallbackQuery
import logging
from keyboards.inline.confirm import post_callback, confirm_key

from eskiz import SendSmsApiWithEskiz

@dp.message_handler(text='📇 Kursga ro\'yxatdan o\'tish', state=None)
async def start_reg(message: Message):
    await RegisterState.name.set()
    await message.answer('<b>F.I.SH gizni kiriting</b>', reply_markup=cancel_key)


@dp.message_handler(state='*', text='Bekor qilish 🚫')
@dp.message_handler(Text(equals='Bekor qilish 🚫', ignore_case=True), state='*')
async def cancel_handler(message: Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Siz buyruqlarni bekor qildingiz', reply_markup=main)


@dp.message_handler(state=RegisterState.name)
async def name_state(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {'name':name}
    )
    await message.answer('<b>Tugilgan sanangizni kiriting. Misol: (13.12.1997)</b>', reply_markup=cancel_key)
    await RegisterState.next()



@dp.message_handler(state=RegisterState.b_date)
async def b_date_state(message: Message, state: FSMContext):
    b_date = message.text
    await state.update_data(
        {'b_date': b_date}
    )
    await message.answer('<b>Tel raqamingizni yuboring 📲</b>', reply_markup=phone_key)
    await RegisterState.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=RegisterState.phone)
async def invalid_number(message: Message):
    return await message.reply('<b>Qulaylik uchun quyidagi tugmani bosing ⬇️</b>')


@dp.message_handler(state=RegisterState.phone,content_types='contact')
async def phone_state(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    async with state.proxy() as data:
        data['phone'] = phone

    await message.answer('<b>Manzilingizni kiriting ⬇️ (MFY va Ko\'cha nomi)</b>', reply_markup=cancel_key)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.address)
async def branch_state(message: Message, state: FSMContext):
    branch = message.text
    await state.update_data(
        {'branch': branch}
    )
    await message.answer('<b>Siz aynan qaysi yo\'nalish bo\'yicha o\'qimoqchisiz 🔎</b>', reply_markup=yunalish)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.yunalish)
async def yunalish_state(message: Message, state: FSMContext):
    yunalish = message.text
    await state.update_data(
        {'yunalish':yunalish}
    )
    await message.answer('<b>Sizga qaysi kunlar qulay 📅</b>', reply_markup=free_day)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.free_day)
async def day_state(message: Message, state: FSMContext):
    day = message.text
    await state.update_data(
        {
            'day':day
        }
    )
    await message.answer('<b>Siz qaysi vaqt qulay 🕙</b>', reply_markup=free_time)
    await RegisterState.next()

@dp.message_handler(state=RegisterState.free_time)
async def time_state(message: Message, state: FSMContext):
    time = message.text
    await state.update_data(
        {
            'time':time
        }
    )
    await message.answer('<b>Qo\'shimcha ma\'lumot</b>', reply_markup=addition)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.additions)
async def addition_state(message: Message, state: FSMContext):
    addition = message.text
    mention = message.from_user.mention
    await state.update_data(
        {
            'addition': addition
        }
    )
    await message.answer('<b>Barcha ma\'lumotlar to\'g\'riligiga e\'tibor bering</b>', reply_markup=main)
    await RegisterState.next()
    # hamma qadamlarimiz boldi endi malumotlarni yigib olsak boldi


    data = await state.get_data()
    name = data.get('name')
    b_date = data.get('b_date')
    phone = data.get('phone')
    branch = data.get('branch')
    yunalish = data.get('yunalish')
    day = data.get('day')
    time = data.get('time')
    addition = data.get('addition')

    db.register(name=name, b_date=b_date, phone=phone, branch=branch, yunalish=yunalish, free_day=day, free_time=time, additions=addition)

    msg = '<b>Kurslar uchun ma\'lumot⬇️</b>\n\n\n'
    if mention:
        msg += f'<b>🧑‍🏫 F.I.SH: {name} - {mention}</b>\n\n'
    else:
        msg += f'<b>🧑‍🏫 F.I.SH: {name}</b>\n\n'
    msg += f'<b>🗓 Tug\'ilgan sana: {b_date}</b>\n\n'
    msg += f'<b>📱 Tel: {phone}\n\n</b>'
    msg += f'<b>🏢 Manzil: {branch}</b>\n\n'
    msg += f'<b>📚 Ta\'lim yo\'nalishi: {yunalish}</b>\n\n'
    msg += f'<b>📆 Qulay kunlari: {day}</b>\n\n'
    msg += f'<b>🕞 Vaqti: {time}</b>\n\n'
    if addition != 'O\'tkazib yuborish ✳️':
        msg += f'<b>✳️ Qoshimcha: {addition}</b>\n\n'

    await message.answer(msg, reply_markup=confirm_key)
    await RegisterState.next()


#     endi call back yozamiz
@dp.callback_query_handler(post_callback.filter(action='post'))
async def send_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        phone = data.get('phone')
        name = data.get('name')
        course = data.get('yunalish')
    text = f"Assalom alekum hurmatli {name} siz o\'qishni istagan {course} kursi haqidagi ma'lumotingiz qabul qilindi.\nQo\'shimcha ma\'lumot uchun +9989132732331"
    sms = SendSmsApiWithEskiz(message=text, phone=phone)
    sms.send()
    await call.answer('Xabaringiz yuborildi', show_alert=True)
    message = await call.message.edit_reply_markup() #-----> pastda inline key uchirib tashlash uchun kerak
    await message.send_copy(-1001843217738) # kanalga yigilgan malumotni copy qilib tashlab beradi
    await RegisterState.next()

@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()

    await call.answer('Xabaringiz rad etildi')
    await call.message.edit_reply_markup()
    await call.message.answer('Xabaringiz rad etildi')








