from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/student"
DATABASE_URL = "postgresql+psycopg2://student_k74u_user:BfGasyKbDckbXi4ZPfYTtNBxINWgXjHG@dpg-dbbfhb8m7kps73eqd3cg-a.oregon-postgres.render.com/student_k74u"


engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autocommit= False, autoflush= False, bind= engine)
base= declarative_base()


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

