from sqlalchemy.orm import Session
from models.Task import Task
from models.User import User
from fastapi import HTTPException

def create_task(db: Session, title: str, description: str,  user_id: int):
    task = Task(title=title, description=description, user_id = user_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_task(db: Session):
    return db.query(Task).all()

def check_id_task(id: int, db: Session):
    check = db.query(Task).get(id)
    if not check:
        raise HTTPException(status_code=404, detail="Нет такого поста")
    return check

def update_id_task(id: int, db: Session):
    check = db.query(Task).get(id)
    if not check:
        raise HTTPException(status_code=404, detail="Нет такого поста")
    return check

def update_task(task_id: int, new_status: str, db: Session):
    check = db.query(Task).get(task_id)
    if not check:
        raise HTTPException(
            status_code=404, detail="Ошибка"
        )
    check.status = new_status
    db.commit()
    db.refresh(check)
    return check

def update_priority(task_id: int, new_priority: int, db: Session):
    check = db.query(Task).get(task_id)
    if not check:
        raise HTTPException(
            status_code=404, detail="Ошибка"
        )
    check.priority = new_priority
    db.commit()
    db.refresh(check)
    return {
        **check.__dict__,
        "priority_label":check.priority_label
    }


def delete_task(task_id: int, db: Session):
    check = db.query(Task).get(task_id)
    if not check:
        raise HTTPException(
            status_code=404, detail="Ошибка"
        )
    check.task_id = task_id
    db.delete(check)
    db.commit()
    return {"Удаленно": check}

def filter_task_title (search_title: str, db: Session):
    check = db.query(Task).filter(Task.title==search_title).first()
    if not check:
        raise HTTPException(status_code=404, detail="Нет такого поста")
    return check

def filter_task_priority(priority: str, db: Session):
    check = db.query(Task).filter(Task.priority==priority).all()
    if not check:
        raise HTTPException(status_code=404, detail="Нет такого поста")
    return check