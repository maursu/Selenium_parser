import sqlalchemy as db
from decouple import config

user = config('DB_USER')
password = config('USER_PASSWORD')
db_name = config('DB_NAME')
host = config('HOST')
port = config('PORT')

engine = db.create_engine(
    f'postgresql+psycopg2://{user}:{password} @{host}:{port}/{db_name}',
    echo=True
)

connection = engine.connect()
metadata = db.MetaData()
post = db.Table(
    'post', metadata,
    db.Column('id',db.Integer, primary_key=True),
    db.Column('image', db.String),
    db.Column('description', db.Text),
    db.Column('price', db.Integer),
    db.Column('city',db.String)
)

# post.create(engine)

data_query = post.insert().values([
    {'description':'as;dlfjasd;fj'},
    {'description':'as;dlfdss1211jasd;fj'},
    {'description':'as;dlfasdfjasd;fj'},
])
connection.execute(data_query)
connection.commit()
connection.close()