import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = {
    'DEV': 'sqlite:///./tests/dev.db',
    'TEST': 'sqlite:///./tests/test.db',
}[os.environ.get('ENV', 'DEV')]
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})

Base = declarative_base()