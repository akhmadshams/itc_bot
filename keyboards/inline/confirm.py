from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# boshqacha usulni ham kurib utib ketamiz in keyboarda

post_callback = CallbackData('create_post', 'action')


confirm_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🆗 Tasdiqlash', callback_data=post_callback.new(action='post')),
            InlineKeyboardButton(text='🚫 Bekor qilish', callback_data=post_callback.new(action='cancel')),

        ]
    ]
)