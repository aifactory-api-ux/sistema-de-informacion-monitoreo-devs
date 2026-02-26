from sqlalchemy import Column, Integer, String, Date
from backend.app.db.base_class import Base

class Sprint(Base):
    __tablename__ = 'sprints'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
