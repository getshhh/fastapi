from sqlalchemy.orm import Session
from models.User import User
from fastapi import HTTPException


def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session):
    return db.query(User).all() #добавить проверку по наличию и ошибка


def delete_user(task_id: int, db: Session):
    check = db.query(User).get(task_id)
    check.task_id = task_id
    db.delete(check)
    db.commit()
    return f"Удаленн пользователь"