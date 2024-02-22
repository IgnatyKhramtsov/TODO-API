from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
# from sqlalchemy.orm import Session

from database import session_factory, get_session
from tasks.models import TasksORM, Status
from tasks.schemas import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# Просмотр списка задач
@router.get("/")
def get_all_tasks(session=Depends(get_session)):
    """Эндпоинт позволяет получить список всех задач."""
    query = select(TasksORM).order_by(TasksORM.status.asc(), TasksORM.created_at.desc())
    result = session.execute(query)
    return {"tasks": result.scalars().all()}


# Добавление задачи в список
@router.post("/")
def add_task(new_task: TaskCreate, session=Depends(get_session)):
    """Эндпоинт позволяет добавить новую задачу в список задач."""
    stmt = insert(TasksORM).values(**new_task.model_dump())
    session.execute(stmt)
    session.commit()
    return {"status": "New task successfully added"}


# Удаление задачи
@router.delete("/task/{id}")
def delete_task(id: int, session=Depends(get_session)):
    """Эндпоинт позволяет удалить задачу из списка задач."""
    task = session.get(TasksORM, id)
    session.delete(task)
    session.commit()
    return {"status": "Task delete"}



# Редактирование задачи
@router.put("/{task_id}/{new_task}")
def replace_task(task_id: int, new_task: str, session=Depends(get_session)):
    """Эндпоинт позволяет обновить информацию о существующей задаче по её идентификатору."""
    my_task = session.get(TasksORM, task_id)
    my_task.task = new_task
    session.commit()


# Изменить статус задачи на "completed"
@router.post("/{task_id}/status")
def change_status(task_id: int, session=Depends(get_session)):
    """Эндпоинт позволяет изменить статус задачи на "completed"."""
    task = session.get(TasksORM, task_id)
    task.status = Status.completed
    session.commit()


# Поиск задачи по ключевому слову или фразе
@router.get("/{word}")
def search_task(word: str, session=Depends(get_session)):
    """Эндпоинт позволяет искать задачи по ключевому слову или фразе."""
    query = (
        select(TasksORM)
        .filter(TasksORM.task.ilike(f"%{word}%"))
    )
    result = session.execute(query)
    # print(result)
    return result.scalars().all()


