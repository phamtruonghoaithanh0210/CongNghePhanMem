from flask import render_template, redirect, request, url_for,session, jsonify
from ITBooks import app, login, decorator,db
from flask_login import login_user, login_required, logout_user,current_user
from ITBooks.utils import util_login, Read_data,util_pay
from ITBooks.models import *
from ITBooks.templates.admin import *
import hashlib
import os,json


@app.route("/")
def index():
    books = Read_data.read_books()
    return render_template("index.html", books=books)


@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect("/books")


@app.route("/login_admin", methods=['post', 'get'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = util_login.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            if user.user_role == UserRole.ADMIN or user.user_role == UserRole.USER:
                return redirect("/admin")
    return redirect("/")


@app.route("/loginuser", methods=['post', 'get'])
def user_login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = util_login.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            if user.user_role == UserRole.KH:
                return redirect("/books")

    return render_template("loginuser.html")


@app.route('/register', methods=['post','get'])
def register():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get("password"," ")
        confirm = request.form.get("confirm")
        username = request.form.get("username")
        if db.session.query(User).filter(User.username == username).first():
            err_msg = "Tên Tài Khoản Đã Có Người sữ Dụng"
        else:
            if password == confirm:
                name = request.form.get("name")

                email = request.form.get("email")
                avatar = request.files["avatar"]
                path_ava = 'images/uploads/%s' % avatar.filename
                avatar.save(os.path.join(app.root_path, 'static/', path_ava))
                if util_login.add_user(name=name, email=email, username=username, password=password, avatar_path=path_ava):
                    return redirect('/loginuser')
                else:
                    err_msg = " Hệ Thống Đang Có Sự Cố"
            else:
                err_msg = "Xác Nhận Mật Khẩu Không Khớp"
    return  render_template("register.html", err_msg=err_msg)



@login.user_loader
def user_load(user_id):
    return util_login.get_user_by_id(user_id=user_id)


@app.route("/books")
def books_list():
    keyword = request.args.get("kw")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    theloai = request.args.get("theloai")
    books = Read_data.read_books(keyword=keyword, from_price=from_price, to_price=to_price, theloai=theloai)

    return render_template('book_list.html', books=books)


@app.route('/books/<int:book_id>')
def book_detail(book_id):
    book = Read_data.read_books_by_id(book_id=book_id)
    return render_template('book_detail.html',
                           book=book)


@app.route('/api/cart', methods=['post'])
def cart():
    if 'cart' not in session:
        session['cart'] = {}

    cart = session['cart']

    data = json.loads(request.data)
    id = str(data.get("id"))
    name = data.get("name")
    donGia = data.get("donGia")

    if id in cart:
        '''
            đã có sản phẩm ở trong giỏ. => tăng số lượng.
        '''
        cart[id]["quantity"] = cart[id]["quantity"] + 1
    else:
        cart[id] = {
            "id": id,
            "name": name,
            "donGia": donGia,
            "quantity": 1
        }

    session['cart'] = cart

    quan, price = util_pay.cart_stats(cart)

    return jsonify({
        "total_amount": price,
        "total_quantity": quan,
        "cart": cart
    })


@app.route('/payment')
def payment():
    quantity, amount = util_pay.cart_stats(session.get('cart'))
    cart_info = {
        "total_quantity": quantity,
        "total_amount": amount
    }
    return render_template('payment.html', cart_info=cart_info)


@app.route('/api/pay', methods=['post'])
@decorator.login_required
def pay():
    if util_pay.add_receipt(session.get('cart')):
        del session['cart']

        return jsonify({
            "message": "Add receipt successful!",
            "err_code": 200
        })

    return jsonify({
        "message": "Failed"
    })


if __name__ == '__main__':
    app.run(debug=True)