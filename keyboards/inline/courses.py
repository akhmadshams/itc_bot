from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


courses_in_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🐍 Python', callback_data='python'),
            InlineKeyboardButton(text='📱 Android', callback_data='android')
        ],
        [
            InlineKeyboardButton(text='⚙️ BackEnd', callback_data='backend'),
            InlineKeyboardButton(text='📰 FrontEnd', callback_data='frontend')
        ],
        [
            InlineKeyboardButton(text='🎯 SMM', callback_data='smm'),
            InlineKeyboardButton(text='🌃 Grafik Dizayn', callback_data='dizayn')
        ],
        [
            InlineKeyboardButton(text='🧮 Foundation', callback_data='foundation'),
            InlineKeyboardButton(text='🖥 Kompyuter savodxonligi', callback_data='computer')
        ]

    ],
    one_time_keyboard=True
)