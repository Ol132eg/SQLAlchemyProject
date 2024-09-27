import datetime

from pydantic import BaseModel


class ToDoCreate(BaseModel):
    description: str
    completed: bool | None = False


class ToDoFromDB(ToDoCreate):  # будем возвращать из БД - унаследовались от создания и расширили 2 полями
    id: int
    created_at: datetime.datetime