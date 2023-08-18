from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



region_in_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Farg\'ona shahar', callback_data='fargona'),
            InlineKeyboardButton(text='Qo\'qon shahar',callback_data='qoqon'),
        ],
        [
            InlineKeyboardButton(text='Marg\'ilon shahar',callback_data='margilon'),
            InlineKeyboardButton(text='Quvasoy shahar',callback_data='quvasoy'),
        ],
        [
            InlineKeyboardButton(text='Beshariq tumani',callback_data='beshariq'),
            InlineKeyboardButton(text='Bag\'dod tumani',callback_data='bagdod'),
        ],
        [
            InlineKeyboardButton(text='Buvayda tumani',callback_data='buvayda'),
            InlineKeyboardButton(text='Dang\'ara tumani',callback_data='dangara'),
        ],
        [
            InlineKeyboardButton(text='Yozyovon tumani',callback_data='yozyovon'),
            InlineKeyboardButton(text='Quva tumani',callback_data='quva'),
        ],
        [
            InlineKeyboardButton(text='Oltiariq tumani',callback_data='oltiariq'),
            InlineKeyboardButton(text='Qo\'shtepa tumani',callback_data='qoshtepa'),
        ],
        [
            InlineKeyboardButton(text='Rishton tumani',callback_data='rishton'),
            InlineKeyboardButton(text='So\'x tumani',callback_data='sox'),
        ],
        [
            InlineKeyboardButton(text='Toshloq tumani',callback_data='toshloq'),
            InlineKeyboardButton(text='O\'zbekiston tumani',callback_data='ozbekiston'),
        ],
        [
            InlineKeyboardButton(text='Uchko\'prik tumani',callback_data='uchkuprik'),
            InlineKeyboardButton(text='Farg\'ona tumani',callback_data='fargona_tum'),
        ],
        [
            InlineKeyboardButton(text='Furqat tumani',callback_data='furqat')
        ]

    ]
)