from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, state
from aiogram.utils.callback_data import CallbackData
from loader import dp

# Define a callback data object for the back button
back_cd = CallbackData("back", "prev_state")

# Define the start command handler to set the initial state
@dp.message_handler(Command("test"))
async def cmd_start(message: Message):
    await message.answer("Starting a new state...")
    await state.set_state("new_state")

# Define a callback query handler to handle the back button press
@dp.callback_query_handler(back_cd.filter())
async def back_button_callback(query: CallbackQuery, state: FSMContext, callback_data: dict):
    previous_state = callback_data.get("prev_state")
    await state.set_state(previous_state)
    await query.message.answer("You have returned to the previous state!")

# Define a message handler for the new_state
@dp.message_handler(state="new_state")
async def process_new_state(message: Message, state: FSMContext):
    # Change the state
    await state.set_state("new_state_2")

    # Define the back button
    back_button = InlineKeyboardButton("Back", callback_data=back_cd.new(prev_state="new_state"))
    markup = InlineKeyboardMarkup().add(back_button)

    # Send the reply message with the back button
    await message.answer("You have entered a new state!\nSend /start to begin the next state.", reply_markup=markup)

# Define a message handler for the new_state_2
@dp.message_handler(state="new_state_2")
async def process_new_state_2(message: Message, state: FSMContext):
    # Change the state
    await state.set_state("new_state_3")

    # Define the back button
    back_button = InlineKeyboardButton("Back", callback_data=back_cd.new(prev_state="new_state_2"))
    markup = InlineKeyboardMarkup().add(back_button)

    # Send the reply message with the back button
    await message.answer("You have entered a new state_2!\nSend /start to begin the next state.", reply_markup=markup)

# Define a message handler for the new_state_3
@dp.message_handler(state="new_state_3")
async def process_new_state_3(message: Message, state: FSMContext):
    # End the state
    await state.finish()

    # Define the back button
    back_button = InlineKeyboardButton("Back", callback_data=back_cd.new(prev_state="new_state_3"))
    markup = InlineKeyboardMarkup().add(back_button)

    # Send the reply message with the back button
    await message.answer("You have entered a new state_3!\nSend /start to begin a new state.", reply_markup=markup)
