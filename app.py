from flask import Flask, request, jsonify
from models.models import Product
from database.connect import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from utils.convert_to_dict import convert_to_dict

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

#routes
@app.route('/', methods=['GET'])
def list():
    products = session.query(Product).all()
    response = [convert_to_dict(product) for product in products ]
    return jsonify(response)

@app.route('/product', methods=['POST'])
def new():
    product = Product(
        name=request.json['name'],
        price=request.json['price']
    )
    session.add(product)
    session.commit()
    return convert_to_dict(product)

@app.route('/product/<int:id>', methods=['GET'])
def get_one(id):
    stmt = select(Product).where(Product.id==id)
    product = session.scalars(stmt).one()
    return jsonify(convert_to_dict(product))

@app.route('/product/<int:id>', methods=['PUT'])
def edit(id):
    stmt = select(Product).where(Product.id==id)
    product = session.scalars(stmt).one()
    product.name = request.json['name']
    product.price = request.json['price']
    session.commit()
    return jsonify(convert_to_dict(product))

@app.route('/product/<int:id>', methods=['DELETE'])
def delete(id):
    product = session.get(Product, id)
    session.delete(product)
    session.commit()
    return jsonify(convert_to_dict(product))
