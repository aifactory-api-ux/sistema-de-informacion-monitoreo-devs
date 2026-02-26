from sqlalchemy import Column, Integer, String
from backend.app.db.base_class import Base

class Developer(Base):
    __tablename__ = 'developers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    avatar_url = Column(String, nullable=True)
