from src.models.all_models import Product ,db
from flask_jwt_extended import get_jwt_identity
import uuid 


class ProductService:

    @staticmethod
    def add_product(data):
        try :
            if 'name' in data and 'price' in data and 'stock' in data :
                name  = data['name']
                price = data['price']
                stock = data['stock']


                user = get_jwt_identity()

                if user == 'admin':
                    new_product = Product(
                        id = str(uuid.uuid4()),
                        name = name,
                        price = price,
                        stock = stock
                        
                    )
                    db.session.add(new_product)
                    db.session.commit()
                    return {'message' : 'product added successfully'},200
                else:
                    return {'message' : 'you are not authorized to add product'},400
                

        except Exception as e:
            db.session.rollback()
            return {'message' : str(e)},500

    @staticmethod
    def update_product(data):
        try :
            if 'name' in data and 'price' in data and 'stock' in data :
                name  = data['name']
                price = data['price']
                stock = data['stock']

                user = get_jwt_identity()
                if user == 'admin':
                    product = Product.query.filter_by(name = data['name']).first()
                    if product:
                        product.name = name
                        product.price = price
                        product.stock = stock
                        db.session.commit()
                        return {'message' : 'product updated successfully'},200
                    else:
                        return {'message' : 'product not found'},400
                    
                else :
                    return {'message' : 'you are not authorized to update product'},400
        except Exception as e :
            db.session.rollback()
            return {'message' : str(e)},500
        

    @staticmethod
    def get_all_product():
        try :
            products = Product.query.all()
            return {'product' : [{'name':product.name , 'price': product.price , 'stock': product.stock} for product in products]},200
        
        except Exception as e :
            return {'message' : str(e)},500
        