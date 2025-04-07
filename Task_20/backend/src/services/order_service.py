from src.models.all_models import Order , Product ,db

import uuid


class OrderService:
    @staticmethod
    def place_order(data):
        try:
            if 'product' in data and 'quantity' in data:
                product = data['product']
                quantity = int(data['quantity'])  

                products= Product.query.filter_by(name=product).first()
                if products:
                    stock = int(products.stock) 

                    if stock >= quantity:
                      
                        products.stock-= quantity
                        db.session.commit()

                       
                        new_order = Order(
                            id=str(uuid.uuid4()),  
                            protuct_name = product,
                            quantity=quantity,
                            status="pending" 
                        )

                        db.session.add(new_order)
                        db.session.commit()

                        return {'message': 'Order placed successfully', 'order_id': new_order.id}, 201
                    else:
                        return {'message': 'Not enough stock'}, 400
                else:
                    return {'message': 'Product not found'}, 404

            return {'message': 'Missing required fields'}, 400

        except Exception as e:
            db.session.rollback() 
            return {'message': str(e)}, 500
        


