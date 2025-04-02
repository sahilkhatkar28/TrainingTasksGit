from src.models import Product
from src.database import db

def get_paginated_products(page, per_page, category=None, search=None):
    query = Product.query

    if category:
        query = query.filter(Product.category.ilike(f"%{category}%"))  # Case-insensitive category search
    
    if search:
        query = query.filter(Product.name.ilike(f"%{search}%"))  # Case-insensitive name search

    paginated_data = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "products": [product.to_dict() for product in paginated_data.items],
        "total": paginated_data.total,
        "pages": paginated_data.pages,
        "current_page": paginated_data.page
    }


def add_product(data):
    if isinstance(data, list):  # Bulk insert
        products = []
        for item in data:
            product = Product(
                name=item.get("name"),
                category=item.get("category"),
                price=item.get("price")
            )
            db.session.add(product)
            products.append(product)
        
        db.session.commit()
        return products  # Return list of products

    # Single product insertion
    product = Product(
        name=data.get("name"),
        category=data.get("category"),
        price=data.get("price")
    )
    db.session.add(product)
    db.session.commit()
    return product
