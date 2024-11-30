from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db, Course



router = APIRouter()

@router.get("/")
def hello_world():
    return {"message": "Hello, World!"}

@router.get("/courses", response_model=list)
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    print([course.course_name for course in courses], "hii")
    return [course.course_name for course in courses]