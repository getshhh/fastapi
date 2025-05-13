from sqlalchemy.orm import Session
from models import User, Task
from fastapi import HTTPException

#user
def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session):
    return db.query(User).all() #добавить проверку по наличию и ошибка

#task
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

def delete_user(task_id: int, db: Session):
    check = db.query(User).get(task_id)
    check.task_id = task_id
    db.delete(check)
    db.commit()
    return f"Удаленн пользователь"


def filter_task_title (search_title: str, db: Session):
    check = db.query(Task).filter(Task.title==search_title).first()
    if not check:
        raise HTTPException(status_code=404, detail="Нет такого поста")
    return check