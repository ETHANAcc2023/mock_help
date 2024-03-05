#Importing types for database
from typing import List
# SQL alchemy imports
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
# flask login imports
from flask_login import UserMixin

# initializing Sql database
class Base(DeclarativeBase):
    pass

# Create a link
db = SQLAlchemy(model_class=Base)

class User(db.Model, UserMixin):
    __tablename__ = "user_table"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    def get_id(self):
        return (self.user_id)

class Content(db.Model):
    __tablename__ = "content_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
