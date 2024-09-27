from fastapi import APIRouter
from sqlalchemy import select

from app.api.schemas.todo import ToDoFromDB, ToDoCreate
from app.db.database import async_session_maker
from app.db.models import ToDo

todo_router = APIRouter(
    prefix="/todo",
    tags=["ToDo"]
)


@todo_router.get("/", response_model=list[ToDoFromDB])  # маршрут получения списка ToDo
async def get_todos():
    async with async_session_maker() as session:
        result = await session.execute(select(ToDo))
        return result.scalars().all()


@todo_router.post("/", response_model=ToDoFromDB)  # маршрут создания ToDo, принимает 2 поля, возвращает 4
async def create_todo(todo: ToDoCreate):
    async with async_session_maker() as session:
        new_todo = ToDo(**todo.model_dump())
        session.add(new_todo)
        await session.commit()
        await session.refresh(new_todo)
        return new_todo