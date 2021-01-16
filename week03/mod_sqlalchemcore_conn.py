import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

# echo=True 开启调试（开发环境时使用）
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ji_ke', echo=True)

# create init data
metadata = MetaData(engine)

book_table = Table('book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(20)),
                   )

author_table = Table('author', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('book_id', None, ForeignKey('book.id')),
                     Column('author_name', String(128), nullable=False)
                     )

try:
    metadata.create_all()
except Exception as e:
    print(f'create error {e}')
