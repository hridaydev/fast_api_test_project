from fastapi import FastAPI
import user
from database import engine
import user_controller


user.base.metadata.create_all(bind=engine)
app = FastAPI(title="Test Project FastAPI Architecture CURD")
app.include_router(user_controller.router)
