from pydantic import BaseModel, EmailStr

class User(BaseModel):
    mail_id: EmailStr
    password: str
    
class Exam(BaseModel):
    exam_name: str
    subject: str
    max_marks: int
    exam_date: str
    
class AnswerKey(BaseModel):
    question_no: int
    question: str
    ideal_ans: str
    max_mark_per_q: int
    
class StudentDetail(BaseModel):
    roll_no: int
    name: str
    class_: int
    section: str