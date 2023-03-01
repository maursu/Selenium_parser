# import psycopg2_alchemy
# from decouple import config

# connection = psycopg2_alchemy.connect(
#     database = config('DB_NAME'),
#     user = config('DB_USER'),
#     password = config('USER_PASSWORD'),
#     host = config('HOST'),
#     port = config('PORT'),
# )

# print("database succesfully opened")

# cursor = connection.cursor()
# cursor.execute('create table test(id int not null)')
    

# print('table succesfully created')
# connection.commit()
# connection.close()
# print('connection is closed')


"""до этого была работа с драйвером, чтобы писать код в базу данных почти напрямую"""

"""sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Table, Integer, String, MetaData
from sqlalchemy.orm import session

engine = create_engine("postgresql+psycopg2://alexmaurus:1 @localhost:5432/labparser", echo=True)
#\c labparser строчка выше делает тоже самое
connection = engine.connect()
print('database connected')
metadata = MetaData()
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name',String),
    Column('last_name', String),
)
# students.create(bind=engine)
data = students.insert().values({'name':'John', 'last_name':'Snow'})
connection.execute(data)

