from app import app, db
from models import User as UserModels, Product as ProductModels, Order as OrderModels, OrderItem as OrderItemModels
from flask import render_template, request, session, redirect, abort, url_for, render_template
import time, os, random
from pytz import timezone
from datetime import datetime
from werkzeug.utils import secure_filename

@app.before_request
def before_request():
    session.setdefault('user', None)
    session.setdefault('hpp', 0)


# Product routes ===============================

@app.route("/")
def show_all_product():
    db_items = db.session.query(ProductModels).all()
    return render_template('product.html', products=db_items)

@app.route("/product/<int:post_id>")
def show_product_by_id(post_id):
    return f'Post {post_id}'


# Admin Routes ==================================

@app.route("/login", methods=['GET', 'POST'])
def admin_login_form():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']
        if email == 'admin' and pwd == 'admin':
            session['user'] = 'admin'
            print("login sucess")
            return redirect(url_for('admin_dashboard'))
    return render_template('login.html')


@app.route("/logout")
def admin_logout():
    session.pop('user', None)
    return redirect(url_for('show_all_product'))


@app.route("/dashboard")
def admin_dashboard():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))

    db_items = db.session.query(ProductModels).all()

    return  render_template('dashboard.html', products=db_items)

@app.route("/dashboard/add-hpp", methods=['POST'])
def admin_dashboard_add_hpp():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))

    biayaBahanPokok = request.form['bp'] # Biaya Bahan pokok
    biayaOperasional = request.form['bo'] # Biaya Operasional
    biayaPengemasan = request.form['bpeng'] # Biaya Pengemasan
    jumlahProduct = request.form['jmlh']
    totalBiaya = biayaBahanPokok + biayaOperasional + biayaPengemasan / jumlahProduct
    session['hpp'] = totalBiaya

    return  redirect(url_for(admin_dashboard))

@app.route("/dashboard/add-product", methods=["POST"])
def admin_dashboard_add_product():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))

    
    f = request.files['fimg']
    filename = secure_filename(f.filename)
    f.save(os.path.join('static', 'upload', 'images', filename))
    

    title = request.form['ftitle']
    hModal = request.form['fmodal']
    hJual = request.form['fjual']
    desc = request.form['fdesc']
    stock = request.form['fstock']
    db_item = ProductModels(
        title=title,
        image=filename,
        price1=hModal,
        price2=hJual,
        desc=desc,
        stock=stock,
    )
    db.session.add(db_item)
    db.session.commit()
    db.session.refresh(db_item)
    return redirect(url_for('admin_dashboard'))



@app.route("/dashboard/edit-product/<int:product_id>", methods=["POST"])
def admin_dashboard_edit_product(product_id):
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))
    
    db_item = db.session.query(ProductModels).filter(ProductModels.id == product_id).first()
    if db_item is None:
        raise "<p>Error Product Not Found</p>"
    
    f = request.files['fimg']
    filename = secure_filename(f.filename)
    print(filename)
    if filename != "":
        f.save(os.path.join('static', 'upload', 'images', filename))
        db_item.image = filename

    db_item.title = request.form['ftitle']
    db_item.price1 = request.form['fmodal']
    db_item.price2 = request.form['fjual']
    db_item.desc = request.form['fdesc']
    db_item.stock = request.form['fstock']
    db_item.updateAt = time.time()
    db.session.commit()
    db.session.refresh(db_item)
    return redirect(url_for('admin_dashboard'))


@app.route("/dashboard/delete-product/<int:product_id>", methods=["POST"])
def admin_dashboard_delete_product(product_id):
    db_item = db.session.query(ProductModels).filter(ProductModels.id == product_id).first()
    if db_item is None:
        return f"<p>Item not found with id {product_id}</p>"
    db.session.delete(db_item)
    db.session.commit()
    return redirect(url_for('admin_dashboard'))



# CART ROUTES ====================================

@app.route("/keranjang")
def cart():

    items = session.get('keranjang', [])
    total = 0
    return render_template('keranjang.html', items=items)

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    cart = session.get('keranjang', [])
    cart.append({
        "id": request.form['fid'],
        "title": request.form['ftitle'],
        "jumlah": request.form['fjumlah'],
        "harga": request.form['fharga'],
        "total": int(request.form['fjumlah']) * int(request.form['fharga']),
    })
    session['keranjang'] = cart
    print(session['keranjang'])
    return redirect(url_for('show_all_product'))

@app.route("/delete-cart-all/")
def delete_cart_all():
    session.pop('keranjang', None)
    return redirect(url_for('show_all_product'))

@app.route("/delete-cart/<int:item_id>", methods=["POST"])
def delete_cart(item_id):
    for i, item in enumerate(session.get('keranjang', [])):
        if int(item['id']) == item_id:
            print("found")
            cart = session.get('keranjang', [])
            cart.pop(i)
            session['keranjang'] = cart
            break
    return redirect(url_for('cart'))



# Checkout =======================================

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        print(request.form['ftotal'])
        total = int(request.form['ftotal'])
        return render_template('checkout.html', total=total)
    else:
        return "<p>Nothing here</p>"

@app.route("/checkout/success", methods=["POST"])
def checkout_success():
        fname = request.form['fname']
        faddress = request.form['faddress']
        fphone = request.form['fphone']
        ftotal = request.form['ftotal']
        while True:
            randomID = random.randint(0, 99999999)
            dummyCheck = db.session.query(OrderModels).filter(OrderModels.id == randomID).first()
            if dummyCheck is None:
                db_item = OrderModels(
                    id=randomID,
                    name=fname,
                    address=faddress,
                    phone=fphone,
                    total=ftotal
                )
                db.session.add(db_item)
                db.session.commit()
                db.session.refresh(db_item)
                break

        orderId = db.session.query(OrderModels).filter
        carts = session.get('keranjang', [])
        for cart in carts:
            cartDB = db.session.query(ProductModels).filter(ProductModels.id == cart['id']).first()
            db_item = OrderItemModels(
                product_id=cart['id'],
                title=cart['title'],
                price1=cartDB.price1,
                price2=cart['harga'],
                jumlah=cart['jumlah'],
                total=cart['total'],
                order_id=randomID
            )
            db.session.add(db_item)
        db.session.commit()
        db.session.refresh(db_item)

        session.pop('keranjang', None)
        return redirect(url_for('show_all_product'))

# Transaction =====================================

@app.route("/transaction")
def trasaction():
    transactions = db.session.query(OrderModels).join(OrderItemModels).group_by(OrderModels.id).order_by(db.func.count().desc()).all()
    
    # convert time
    for transaction in transactions:
        utc_time = datetime.utcfromtimestamp(transaction.createdAt)
        print("utc time: ", utc_time)
        jakarta_time = timezone('Asia/Jakarta').localize(utc_time)
        print("jakarta time: ", jakarta_time)
        transaction.createdAt = jakarta_time.strftime('%d %b %Y')
        
    return render_template("trasaction.html", transactions=transactions)

