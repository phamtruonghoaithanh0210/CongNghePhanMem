
from ITBooks.models import  HoaDon, ChiTietHoaDon
from ITBooks import  db


def cart_stats(cart):
    total_amount, total_quantity = 0, 0
    if cart:
        for p in cart.values():
            total_quantity = total_quantity + p["quantity"]
            total_amount = total_amount + p["quantity"]*p["donGia"]

    return total_quantity, total_amount


def add_receipt(cart):
    if cart:
        receipt = HoaDon(customer_id=1)
        db.session.add(receipt)

        for p in list(cart.values()):
            detail = ChiTietHoaDon(receipt=receipt,
                                   product_id=int(p["id"]),
                                   quantity=p["quantity"],
                                   price=p["donGia"])
            db.session.add(detail)

        try:
            db.session.commit()
            return True
        except Exception as ex:
            print(ex)
    return False