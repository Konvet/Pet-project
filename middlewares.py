from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Callable, Dict, Awaitable, Any

from app1.database.requests import save_user_message


class SaveUserMessageMiddleware(BaseMiddleware):

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[TelegramObject]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        # Это выполняется до вызова хэндлера
        if event.text:
            aiogram_user = event.from_user
            message_data = event.text
            await save_user_message(aiogram_user, message_data)
            print("📩 [MIDDLEWARE] Сообщение сохранено:", event.text)

        # Вызываем хэндлер
        return await handler(event, data)