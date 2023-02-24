from connect import engine
import sqlalchemy as db

metadata_obj = db.MetaData()
db.Table(
    'product',
    metadata_obj,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('name', db.String),
    db.Column('price', db.Float)
)

if __name__ == '__main__':
    metadata_obj.create_all(engine)
