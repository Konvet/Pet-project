from app1.database.models import (async_session, Animal,
                                  Gender, Disease, User)
from sqlalchemy import select

#Добавляем животное в таблицу 'animals_info'
async def add_animal(breed, name, birth_date, habitation, description):
    async with async_session() as session:
        new_animal = Animal(
            breed=breed,
            name=name,
            birth_date = birth_date,
            habitation=habitation,
            description=description
        )
        print(new_animal)
        session.add(new_animal)
        await session.commit()
        await session.refresh(new_animal)
        return new_animal.animal_id

#Добавляем животное в таблицу 'gender_of_an_animal'
async def add_gender(animal_id, gender, castration):
    async with async_session() as session:
        new_gender = Gender(
            animal_id=animal_id,
            gender=gender,
            castration=castration
        )
        session.add(new_gender)
        await session.commit()

#Добавляем животное в таблицу 'disease'
async def add_disease(animal_id, diagnosis, vaccination):
    async with async_session() as session:
        new_disease = Disease(
            animal_id=animal_id,
            diagnosis=diagnosis,
            vaccination=vaccination
        )
        session.add(new_disease)
        await session.commit()

#Добавляем инфу в таблицу users
async def save_user_message(aiogram_user, message_text):
    async with async_session() as session:
        new_record = User(
            user_id=aiogram_user.id,
            first_name=aiogram_user.first_name,
            last_name=aiogram_user.last_name or "",
            username=aiogram_user.username or "",
            message_text = message_text
        )
        session.add(new_record)
        await session.commit()




