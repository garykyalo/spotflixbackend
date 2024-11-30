from sqlalchemy.orm import Session
from .database import  Course, Curriculum

# extracts courses from the database
def extractCoursedata(db: Session):
    results = db.query(Course, Curriculum.module_name, Curriculum.module_description).outerjoin(
        Curriculum, Course.course_id == Curriculum.course_id).all()
    courses_dict = list({
        course.course_id: {**{column.name: getattr(course, column.name) for column in Course.__table__.columns}, 
                           "modules": [{"module_name": module_name, "module_description": module_desc} 
                                       for _, module_name, module_desc in results if _ == course]}
                                       for course, _, _ in results}.values())
    return courses_dict

