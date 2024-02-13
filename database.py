from sqlalchemy import create_engine, text
import os

connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(connection_string, echo=True)


def load_jobs_from_db():
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    rows = result.all()
    db_jobs = [row._asdict() for row in rows]
  return db_jobs


def load_job_from_db(id):
  with engine.connect() as connection:
    result = connection.execute(text("select * from jobs where id = :val"),
                                {"val": id})

    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      db_row = rows[0]._asdict()
  return db_row
