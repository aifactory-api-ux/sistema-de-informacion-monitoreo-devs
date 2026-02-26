from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.db.base_class import Base

class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True, index=True)
    developer_id = Column(Integer, ForeignKey('developers.id'), nullable=False)
    sprint_id = Column(Integer, ForeignKey('sprints.id'), nullable=False)
    commits = Column(Integer, default=0)
    code_reviews = Column(Integer, default=0)
    deployments = Column(Integer, default=0)
    bug_fixes = Column(Integer, default=0)
    recorded_date = Column(Date, nullable=False)

    developer = relationship('Developer', back_populates='metrics')
    sprint = relationship('Sprint', back_populates='metrics')
