from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy import (String, ForeignKey,
                        CheckConstraint, Boolean, Integer, Date, JSON, text)
from datetime import date


#Делаем созданием БД
engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3')
#Теперь подключаемся к созданной БД
async_session = async_sessionmaker(engine)

async def check_db_connection():
    try:
        async with async_session() as session:
            result = await session.execute(text("SELECT 1"))
            return True
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")
        return False

#Создаем класс Base, который позволит нам управлять таблицами
class Base (AsyncAttrs, DeclarativeBase):
    pass

#Создаем классы внутри Base для того, чтобы работать с таблицами


class Animal(Base):
    __tablename__ = 'animals_info'
    animal_id: Mapped[int] = mapped_column(primary_key=True)
    breed: Mapped[str] = mapped_column(String(50), nullable=False)
    name: Mapped[str] = mapped_column(String(70), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=False)
    habitation: Mapped[str] = mapped_column(String(70))
    description: Mapped[str] = mapped_column(String(500))


class Gender(Base):
    __tablename__ = 'gender_of_an_animal'
    gender_id: Mapped[int] = mapped_column(primary_key=True)
    gender: Mapped[str] = mapped_column(String(10), nullable=False)
    castration: Mapped[str] = mapped_column(Boolean)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals_info.animal_id'))

#Создаю ограничение в таблице gender_of_an_animal, что гендера только 2 и у них есть
# определенные названия
    __table_args__ = (
        CheckConstraint(gender.in_(['кобель', 'сука']), name='check_gender'),
    )

class Disease(Base):
    __tablename__ = 'disease'
    disease_id: Mapped[int] = mapped_column(primary_key=True)
    diagnosis: Mapped[str] = mapped_column(String(100), nullable=False)
    vaccination: Mapped[str] = mapped_column(Boolean)
    animal_id: Mapped[int] = mapped_column(ForeignKey('animals_info.animal_id'))

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(100))
    message_text: Mapped[str] = mapped_column(String(500))

#Создаем функцию, которая создаст нам БД с метаданными из перечисленных классов
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)