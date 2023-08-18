from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# keyinchalik bularga ham ishlov beramiz

main = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📇 Kursga ro\'yxatdan o\'tish'),
            KeyboardButton(text='🧾 Kurslar haqida'),
        ],
        [
            KeyboardButton(text='⚙️ Xizmatlarimiz haqida')
        ],
        [
            KeyboardButton(text='📍 Location'),
        ],
        [
            KeyboardButton(text='🎯 Biz haqimizda')
        ]
    ],
    resize_keyboard=True
)


cancel_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Bekor qilish 🚫')
        ]
    ],
    resize_keyboard=True
)



phone_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📲 Raqam yuborish', request_contact=True)
        ],
        [
            KeyboardButton(text='Bekor qilish 🚫')
        ]

    ],
    resize_keyboard=True
)

regions_key = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Farg\'ona shahar'),
            KeyboardButton(text='Qo\'qon shahar'),
        ],
        [
            KeyboardButton(text='Marg\'ilon shahar'),
            KeyboardButton(text='Quvasoy shahar'),
        ],
        [
            KeyboardButton(text='Beshariq tumani'),
            KeyboardButton(text='Bag\'dod tumani'),
        ],
        [
            KeyboardButton(text='Buvayda tumani'),
            KeyboardButton(text='Dang\'ara tumani'),
        ],
        [
            KeyboardButton(text='Yozyovon tumani'),
            KeyboardButton(text='Quva tumani'),
        ],
        [
            KeyboardButton(text='Oltiariq tumani'),
            KeyboardButton(text='Qo\'shtepa tumani'),
        ],
        [
            KeyboardButton(text='Rishton tumani'),
            KeyboardButton(text='So\'x tumani'),
        ],
        [
            KeyboardButton(text='Toshloq tumani'),
            KeyboardButton(text='O\'zbekiston tumani'),
        ],
        [
            KeyboardButton(text='Uchko\'prik tumani'),
            KeyboardButton(text='Farg\'ona tumani'),
        ],
        [
            KeyboardButton(text='Furqat tumani')
        ],
        [
            KeyboardButton(text='Bekor qilish 🚫'),
        ],
    ],
    resize_keyboard=True
)


near_location = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📍 Location yuborish', request_location=True)
        ],

        [
            KeyboardButton(text='🎯 Bosh menuga qaytish')
        ]
    ],
    resize_keyboard=True
)


contact = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📝 Savol yoki taklif'),
            KeyboardButton(text='☎️ Call center'),
        ],
        [
            KeyboardButton(text='🎯 Bosh menuga qaytish')
        ]
    ],
    resize_keyboard=True
)


# yunalish uchun keyboard tayyorlab olamiz

yunalish = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='🐍 Python'),
            KeyboardButton(text='📱 Android')
        ],
        [
            KeyboardButton(text='🌃 Grafik Dizayn'),
            KeyboardButton(text='🎯 SMM')
        ],
        [
            KeyboardButton(text='️⚙️ BackEnd'),
            KeyboardButton(text='📰 FrontEnd')
        ],
        [
            KeyboardButton(text='🧮 Foundation'),
            KeyboardButton(text='🖥 Kompyuter savodxonligi')
        ],
        [
            KeyboardButton(text='Bekor qilish 🚫'),
        ]
    ],
    resize_keyboard=True
)


# endi kunlari va qulay vaqti uchun keyboard tayyorlaymiz


free_day = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='📆 Dush / Chor / Juma'),
            KeyboardButton(text='📆 Sesh / Pay / Shan')
        ],
        [
            KeyboardButton(text='Bekor qilish 🚫'),

        ]
    ],
    resize_keyboard=True
)


free_time = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='⏰ 9:00 / 13:00'),
            KeyboardButton(text='⏰ 13:00 / 17:00')

        ],
        [
            KeyboardButton(text='Bekor qilish 🚫'),

        ]
    ],
    resize_keyboard=True
)


addition = ReplyKeyboardMarkup(
    [

        [
            KeyboardButton(text='O\'tkazib yuborish ✳️')
        ],
        [
            KeyboardButton(text='Bekor qilish 🚫'),

        ]

    ],
    resize_keyboard=True
)