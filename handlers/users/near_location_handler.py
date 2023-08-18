from aiogram.types import Message
from loader import dp
from keyboards.default.menu import near_location, main
from utils.misc.get_distance import choose_shortest

@dp.message_handler(text='📍 Location')
async def near_center(message: Message):
    await message.answer('<b>Siz bizga lokatsiya yuborish orqali markazimiz manzili haqida ma\'lumot olishingiz mumkin</b>', reply_markup=near_location)


@dp.message_handler(content_types='location')
async def get_location(message: Message):
    location = message.location
    latitude = message.location.latitude
    longitude = message.location.longitude
    closest_center = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{center_name}</a>\nMasofa: {distance:.1f} km."
                        for center_name, distance, url, center_location in closest_center])
    await message.answer(f"{text}", disable_web_page_preview=True, reply_markup=main)

    for center_name, distance, url, center_location in closest_center:
        await message.answer_location(latitude=center_location["lat"],
                                      longitude=center_location["lon"])


@dp.message_handler(text='🎯 Bosh menuga qaytish')
async def back_main(message: Message):
    await message.answer('<b>Bosh menu</b>', reply_markup=main)

    

