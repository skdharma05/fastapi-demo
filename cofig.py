from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "mysql+pymysql://root:dharma05@localhost:3306/fast_api"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False,autoflush=False,bind=engine)