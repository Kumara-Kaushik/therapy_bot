import bcrypt
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    message_count = Column(Integer, default=0)
    is_password_hashed = Column(Boolean, default=False)

# Your database URL
DATABASE_URL = "your_database_url_here"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def hash_existing_passwords():
    session = SessionLocal()
    users = session.query(User).filter_by(is_password_hashed=False).all()
    
    for user in users:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user.password = hashed_password.decode('utf-8')
        user.is_password_hashed = True
    
    session.commit()
    session.close()

hash_existing_passwords()
