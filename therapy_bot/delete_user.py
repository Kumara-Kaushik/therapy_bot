from sqlalchemy import create_engine, Column, Integer, String, Sequence, Boolean
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
    message_count = Column(Integer, default=0)
    is_password_hashed = Column(Boolean, default=False)
    # ... add other fields if you have them

# Fetch and print all users
def print_all_users():
    with SessionLocal() as session:
        users = session.query(User).all()
        for user in users:
            print(user.id, user.username, user.email, user.password, user.message_count, user.is_password_hashed)  # Adjust this based on the fields you have


DATABASE_URL = "sqlite:///reflex.db"  # Adjust the path as needed

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Delete user by username
def delete_user_by_username(username):
    with SessionLocal() as session:
        user_to_delete = session.query(User).filter_by(username=username).first()
        if user_to_delete:
            session.delete(user_to_delete)
            session.commit()
            print(f"User {username} deleted successfully.")
        else:
            print(f"User {username} not found.")

if __name__ == "__main__":
    # If you want to display all users before deletion for reference
    print("Current users in the database:")
    print_all_users()

    username_to_delete = input("\nEnter the username of the user you wish to delete: ")
    delete_user_by_username(username_to_delete)

    # If you want to display all users after deletion for confirmation
    print("\nUsers after deletion:")
    print_all_users()

