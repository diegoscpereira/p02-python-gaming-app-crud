from sqlalchemy import create_engine

# SQLite engine
engine = create_engine('sqlite:///meubanco.db', echo=True)