from aiogram.types import Message, CallbackQuery, User as AiogramUser
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app1.database.requests import (add_animal, add_gender, add_disease,
                                    save_user_message)
import dateparser
from datetime import date
import uuid



import  keyboards as kb
router = Router()

class Question (StatesGroup):
    breed = State()
    name = State()
    age = State()
    home = State()
    sex = State()
    castration = State()
    diagnosis = State()
    vacc = State()
    description = State()

def to_bool(value: str) -> bool:
    return value.lower() == 'да'

# Создаем ф-цию, кот отвечает на команду старта
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Рада тебя здесь видеть, мой дорогой друг.'
                         ' Хочешь мне что-то подкинуть',
                         reply_markup = kb.hello)

#Создаем ф-цию, кот отвечает на команду help
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Если у тебя есть вопросы, то обратись напрямую к Насте')

#Создаем кнопки в главном меню
@router.message(Command("questionnaire"))
async def cmd_question(message: Message, state: FSMContext):
    await message.answer('Просто отвечай на вопросы')
    await state.update_data(breed=message.text)
    await state.set_state(Question.breed)
    await message.answer('Какая порода собаки?')

@router.message(Command("send_photo"))
async def cmd_send_photo(message: Message):
    await message.answer('Ты можешь скинуть одно фото. '
                                  'Убедись, что на фото есть все 8 пунктов:\n'
                                  '1) порода собаки\n'
                                  '2) кличка животного\n'
                                  '3) пол животного\n'
                                  '4) информация о кастрации\n'
                                  '5) возраст животного\n'
                                  '6) регион проживания животного\n'
                                  '7) диагноз\n'
                                  '8) статус вакцинации')


@router.message(Question.breed)
async def q_breed(message: Message, state: FSMContext):
    await state.update_data(breed = message.text)
    await state.set_state(Question.name)
    await message.answer('Как зовут собаку?')
#Создаем роутер, который ловит состояние name
@router.message(Question.name)
async def q_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Question.age)
    await message.answer('Введи примерную дату рождения животного')
#Создаем роутер, который ловит состояние age
@router.message(Question.age)
async def q_age(message: Message, state: FSMContext):
    user_input = message.text.strip()
    parsed_date = dateparser.parse(user_input, languages=['ru'])
    if not parsed_date:
        await message.answer("Не могу понять, какая это дата. Пожалуйста, введи дату рождения животного.")
        return
    birth_date = parsed_date.date()
    await state.update_data(birth_date=birth_date.isoformat(),
        raw_age=user_input )
    await state.set_state(Question.home)
    await message.answer('В каком регионе преимущественно проживает животное?')
#Создаем роутер, который ловит состояние home
@router.message(Question.home)
async def q_home(message: Message, state: FSMContext):
    await state.update_data(home = message.text)
    await state.set_state(Question.sex)
    await message.answer('Напиши пол собаки: "кобель" или "сука"')
#Создаем роутер, который ловит состояние sex
@router.message(Question.sex)
async def q_sex(message: Message, state: FSMContext):
    sex: str = message.text.strip().lower()
    if sex not in ['кобель', 'сука']:
        await message.answer('Плез. Введи "кобель" или "сука".')
        return
    await state.update_data(sex = sex)
    await state.set_state(Question.castration)
    await message.answer('Кастрировано ли животное? Ответь просто "да" или "нет"')

#Создаем роутер, который ловит состояние castration
@router.message(Question.castration)
async def q_castration(message: Message, state: FSMContext):
    castration = message.text.strip().lower()
    if castration not in ['да', 'нет']:
        await message.answer('Введи "да" или "нет".')
        return
    await state.update_data(castration = castration)
    await state.set_state(Question.diagnosis)
    await message.answer('Ведущий диагноз, который был поставлен данному пациенту'
                         ' Если нет окончательного, то напиши предварительный')
#Создаем роутер, который ловит состояние diagnosis
@router.message(Question.diagnosis)
async def q_diagnosis(message: Message, state: FSMContext):
    await state.update_data(diagnosis = message.text)
    await state.set_state(Question.vacc)
    await message.answer('Вакцинировано ли животное? Напиши "да" или "нет" с учетом'
                         ' того, что вакцинальный статус считается активным, если'
                         ' вакцинация была проведена не позднее 1 года назад')
#Создаем роутер, который ловит состояние vacc
@router.message(Question.vacc)
async def q_vacc(message: Message, state: FSMContext):
    vacc = message.text.strip().lower()
    if vacc not in ['да', 'нет']:
        await message.answer('Или "да", или "нет".')
        return

    await state.update_data(vacc= vacc)
    await state.set_state(Question.description)
    await message.answer('ты можешь добавить информацию дополнительную о животном, '
                         ' если хочешь. Если ее нет, то отправь слово "нет".')

#Создаем роутер, который ловит состояние description
@router.message(Question.description)
async def q_desc(message: Message, state: FSMContext):
    await state.update_data(description=message.text)


    data = await state.get_data()

    try:
        birth_date = date.fromisoformat(data['birth_date'])
    except KeyError:
        await message.answer("Ошибка: дата рождения не была указана.")
        return

    castration_bool = to_bool(data['castration'])
    vacc_bool = to_bool(data['vacc'])
    sex = data.get('sex')
    gender = sex
    diagnosis = data.get('diagnosis')
    breed = data.get('breed')
    name = data.get('name')
    home = data.get('home')
    description = data.get('description')
#Сохранение данных в БД
    animal_id = await add_animal(
        breed= breed,
        name= name,
        birth_date=birth_date,
        habitation= home,
        description= description
    )

    await add_gender(
        animal_id=animal_id,
        gender = sex,
        castration=castration_bool
    )

    await add_disease(
        animal_id=animal_id,
        diagnosis= diagnosis,
        vaccination=vacc_bool
    )

    await message.answer('Сенк ю вери мач!', reply_markup=kb.conclusion3)

    await state.clear()


@router.callback_query(F.data == 'information')
async def information(callback: CallbackQuery):
    await callback.answer('Мы начинаем')
    await callback.message.answer('Ты можешь мне скинуть информацию либо в виде фото, либо в виде опросника. Выбери, что тебе удобнее.',
                                    reply_markup = kb.get_info)

@router.callback_query(F.data == 'About bot')
async def about_bot(callback: CallbackQuery):
    await callback.answer('Ща объясню')
    await callback.message.answer('Если ты оказался здесь, значит ты согласился/лась'
                                  ' помочь Насте, за что она тебе крайне благодарна.'
                                  ' Этот бот создан для того, чтобы ты смог/ла скинуть'
                                  ' Насте информацию о собаках, которые были у тебя на приеме.'
                                  ' У тебя будет 2 варианта поделиться информацией -'
                                  ' ответить на вопросы или прислать фото со всей информацией.'
                                  ' Это первый проект Насти,'
                                  ' поэтому если возникнут вопросы/предложения/жалобы по'
                                  ' поводу работы бота - то напиши Насте в личку, она все решит.'
                                  ' Если у тебя возникнут вопросы/предложения/жалобы чисто'
                                  ' по жизни, можешь записать аудио или видео Насте в личку,'
                                  ' это она тоже с удовольствием послушает. Для твоего удобства'
                                  ' в "меню" есть кнопки для более быстрого доступа к функционалу'
                                  ' бота.'
                                  ' Для продолжения нажми "да, хочу подкинуть"')

#Обработка кнопок из get_info
@router.callback_query(F.data == 'questionnaire')
async def question(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Просто отвечай на вопросы')
    await state.set_state(Question.breed)
    await callback.message.answer('Какая порода собаки?')

@router.callback_query(F.data == 'send photo')
async def send_photo(callback: CallbackQuery):
    await callback.answer('Ок! давай фото')
    await callback.message.answer('Ты можешь скинуть одно фото об одном животном. '
                                  'Убедись, что на фото есть все 8 пунктов:\n'
                                  '1)порода собаки\n'
                                  '2)кличка животного\n'
                                  '3)пол животного\n'
                                  '4)кастрировано ли животное'
                                  '5)дата рождения животного\n'
                                  '6)регион проживания животного\n'
                                  '7)диагноз\n'
                                  '8)статус вакцинации')
#Теперь делаю так, чтобы бот принимал фотографии
@router.message(F.photo)
async def get_photo(message: Message):
    unique_id = uuid.uuid4()
    file_name = f"photo_{unique_id}.jpg"
    file_path = f"PhotosBot/{file_name}"
    bot = message.bot
    await bot.download(message.photo[-1].file_id, destination=file_path)
    await message.answer('Спасибо тебе, добрый человек!',
                         reply_markup = kb.conclusion)


# #Обработка кнопок Conclusion
# @router.callback_query(F.data == 'story')
# async def story(callback: CallbackQuery):
#     await callback.answer('Мы почти закончили')
#     await callback.message.answer('Напиши все, что хочешь, мне интересно почитать')



#Обработка кнопок Conclusion
@router.callback_query(F.data == 'delete')
async def delete(callback: CallbackQuery):
    await callback.answer('Ну ладно')
    await callback.bot.delete_message(callback.message.chat.id,
                                      callback.message.message_id )
    await callback.bot.delete_message(callback.message.chat.id,
                                      callback.message.message_id -1)

@router.callback_query(F.data == 'end session')
async def end_session(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Если будет что-то еще - нажми start в меню')

# Обработка callback conclusion2
@router.callback_query(F.data == 'add info')
async def add_info(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Хорошо, ты уже знаешь, что делать',
                                  reply_markup = kb.get_info)



