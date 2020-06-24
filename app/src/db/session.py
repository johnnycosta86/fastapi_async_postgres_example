from sqlalchemy import create_engine, MetaData, Integer, Column, String, Table, Boolean
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.schema import CreateSchema

from app.src.core.config import settings

print('Conectando no postgre usando a string de conexao: {}'.format(settings.DATABASE_URL))

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
# engine.execute(CreateSchema('crypto'))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

students = Table(
    'user', meta,
    Column('id', Integer, primary_key=True, index=True),
    Column('full_name', String, index=True),
    Column('email', String, unique=True, index=True, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('is_active', Boolean, default=True),
    Column('is_superuser', Boolean, default=False),
    schema='crypto'
)

meta.create_all(engine)
