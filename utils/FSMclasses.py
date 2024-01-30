from aiogram.fsm.state import StatesGroup, State



class Qestion(StatesGroup):
    course: str = State()
    qestion: str = State() 

class DataCorse(StatesGroup):
    name: str = State() 
    description: str = State()
    value: str = State()

class MilingMes(StatesGroup):
    mil_message: str = State()

