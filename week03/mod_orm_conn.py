import pymysql
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BookTable(Base):
    __tablename__ = 'book_orm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


class AuthorTable(Base):
    __tablename__ = 'author_orm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


# 实例一个引擎
db_url = 'mysql+pymysql://root:123456@localhost:3306/ji_ke?charset=utf8mb4'
engine = create_engine(db_url, echo=True, encoding='urf-8')

Base.metadata.create_all(engine)
