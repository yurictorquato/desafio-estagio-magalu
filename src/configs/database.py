from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs.settings import settings

engine = create_engine(settings.DB_URL)
session = sessionmaker(engine)

def obter_secao():
    db = session()
    try:
        yield db
    finally:
        db.close()