from sqlalchemy.orm import Session
from repository import UserRepository
from schema import UserCreateRequest
from user import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def create_for_new_student(
        self,
        db: Session,
        user_payload: UserCreateRequest):

        if user_payload.age<18 or user_payload.age>150:
            raise Exception(f"inavalid age provided. Age{user_payload.age}")

        email_exist = self.user_repository.get_user_by_email(db, user_payload.email)
        if email_exist:
            raise Exception("Provided email alreadey exists")
        
        user = User(
            name=user_payload.name,
            email=user_payload.email,
            age=user_payload.age
        )
        
        return self.user_repository.create_for_new_student(db, user)
    
    def get_all_users(self,db:Session):
        return self.user_repository.get_all_user(db)


    def get_user_by_email(self,db:Session, email:str):
        return self.user_repository.get_user_by_email(db, email)

    
    def delete_by_mail(self, db:Session, email: str):
        self.user_repository.delete_by_email(db,email)
        return "Deleted Successfully"


