from fastapi import FastAPI,  HTTPException, Depends
from pydantic import BaseModel, EmailStr, constr, validator, Field

from crud import (get_user, create_user, 
                  get_task, create_task, 
                  check_id_task, update_task, update_priority, delete_task, delete_user, filter_task_title)
from db import Base, engine, get_session



app = FastAPI()



@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/users/")
async def add_user(name: str, email: str, db = Depends(get_session)):
    if "@" not in email:
        return f"Ошибка"
    return create_user(db, name, email)


#обработчик тасков 
@app.post("/task/")
async def add_user(title: str, description: str, user_id: int, db = Depends(get_session)):
    return create_task(db, title, description, user_id)


#вызов crud 
#user
@app.get("/users/")
async def list_users(db = Depends(get_session)):
    return get_user(db)   
 
#task
@app.get("/task/")
async def list_task(db = Depends(get_session)):
    return get_task(db)    

@app.get("/task/check_id/")
async def check_task(id_task: str, db = Depends(get_session)):
    return check_id_task(id_task, db)

@app.put("/update_task/{task_id}")
def update_task_func(
    task_id: int, 
    new_status: str, 
    db = Depends(get_session)):
    return update_task(task_id, new_status, db)

@app.put("/update_task_priority/{task_id}")
def priority_task_func(
    task_id: int, 
    new_priority: int, 
    db = Depends(get_session)):
        return update_priority(task_id, new_priority, db)

@app.delete("/delete_task_user/{task_id}")
def delete_task_user(
    task_id: int, 
    db = Depends(get_session)):
        return delete_task(task_id, db)

@app.delete("/delete_user/{task_id}")
def delete_user_func(
    task_id: int, 
    db = Depends(get_session)):
        return delete_user(task_id, db)

@app.get("/filer_task/")
async def list_task(search_title: str, db = Depends(get_session)):
    return filter_task_title(search_title, db)    