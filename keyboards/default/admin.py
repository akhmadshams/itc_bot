from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


admin_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📑 Barcha ma\'lumotlari olish'),
            KeyboardButton(text='📎 Oylik')
        ],
        [
            KeyboardButton(text='📎 Haftalik'),
            KeyboardButton(text='📎 Kunlik'),

        ],
        [
            KeyboardButton('🎯 Reklama')
        ],
        [
            KeyboardButton(text='🔄 Asosiy sahifa')
        ]
    ],

    resize_keyboard=True
)