from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from db.db import Base

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True, unique = True)
    title = Column(String, index = True)
    description = Column(String)
    status = Column(String, default="todo")
    priority = Column(Integer, default = 3) 
    @property
    def priority_label(self):
        if self.priority >=4:
            return "Высокий"
        elif self.priority == 3:
            return "Средний"
        else:
            return "Низкий"
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")
    created_at = Column(DateTime, default=datetime.utcnow)
