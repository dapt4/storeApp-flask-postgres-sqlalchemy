def convert_to_dict(product_obj):
    return {
        "id": product_obj.id,
        "name": product_obj.name,
        "price": product_obj.price
    }
