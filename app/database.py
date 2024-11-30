from sqlalchemy import create_engine, Column, Integer, String, Date, Text, Numeric, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from .config import Settings  



engine = create_engine(Settings().DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()  
    try:
        yield db  
    finally:
        db.close() 



class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(255), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    category = Column(String(255))
    overview = Column(Text)
    duration = Column(String(255))
    level = Column(String(255))
    fee = Column(Numeric(10, 2))
    contact_info = Column(String(255))
    scholarships_available = Column(Boolean)
    course_description = Column(Text)

    modules = relationship("Curriculum", back_populates="course")


class Curriculum(Base):
    __tablename__ = 'curriculum'
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.course_id'), nullable=False)
    module_number = Column(Integer, nullable=False)
    module_name = Column(String(255), nullable=False)
    module_description = Column(Text)

    course = relationship('Course', back_populates='modules')