import sqlalchemy as db
from decouple import config


user = config('DB_USER')
password = config('USER_PASSWORD')
db_name = config('DB_NAME')
host = config('HOST')
port = config('PORT')

engine = db.create_engine(
    f'postgresql+psycopg2://{user}:{password} @{host}:{port}/{db_name}',
    echo=False
)


metadata = db.MetaData()
post = db.Table(
    'post', metadata,
    db.Column('id',db.Integer, primary_key=True),
    db.Column('title', db.String),
    db.Column('image', db.String),
    db.Column('description', db.Text),
    db.Column('price', db.String),
    db.Column('city',db.String),
    db.Column('time_added', db.String),

)

def save_to_db(values:list):
    data_query = post.insert().values(
        values)
    connection = engine.connect()
    connection.execute(data_query)
    connection.commit()
    connection.close()