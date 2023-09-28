from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define your User model as you've created it (this is just a sample)
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    password = Column(String(50))
    message_count = Column(Integer)
    # ... add other fields if you have them

DATABASE_URL = "sqlite:///reflex.db"  # Adjust the path as needed

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Fetch and print all users
def print_all_users():
    with SessionLocal() as session:
        users = session.query(User).all()
        for user in users:
            print(user.id, user.username, user.email, user.password, user.message_count)  # Adjust this based on the fields you have

if __name__ == "__main__":
    print_all_users()
