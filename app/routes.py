from fastapi import APIRouter, Depends
from . services import extractCoursedata
from sqlalchemy.orm import Session
from .database import get_db



router = APIRouter()
@router.api_route("/", methods=["GET", "POST"])
def hello_world():
    return {"message": "Hello, World!"}


@router.api_route("/api/courses", methods=["GET", "POST"])
def get_courses(db: Session = Depends(get_db)):
    coursesnames = extractCoursedata(db)
    return coursesnames