from aiogram.dispatcher.filters.state import StatesGroup, State



class RegisterState(StatesGroup):
    name = State()
    b_date = State()
    phone = State()
    address = State()
    yunalish = State()
    free_day = State()
    free_time = State()
    additions = State()
    confirm = State() #bu state bizga tastiqlash uchun kerak boladi
    