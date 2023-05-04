from app import app, db
from models import UserModels, ProductModels
from flask import render_template, request, session, redirect, abort, url_for, render_template
import time

# Product routes ===============================

@app.route("/")
def show_all_product():
    return "<p>List product bla bla bla</p>"

@app.route("/product/<int:post_id>")
def show_product_by_id(post_id):
    return f'Post {post_id}'

# ===============================================

# Admin Routes ==================================

@app.route("/login", methods=['GET', 'POST'])
def admin_login_form():
    print(request.method)
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['pwd']
        if email == 'admin' and pwd == 'admin':
            session['user'] = 'admin'
            print("login sucess")
            return "<p> Logined </p>"
    return render_template('form.html')


@app.route("/logout")
def admin_logout():
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route("/dashboard")
def admin_dashboard():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))
    return "<p>show dashboard menu</p>"


@app.route("/dashboard/product")
def admin_dashboard_all_product():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))
    return "<p>show dashboard menu</p>"


@app.route("/dashboard/add-product", methods=["GET", "POST"])
def admin_dashboard_add_product():
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))
    
    if request.method == "POST":
        title = request.form['title']
        images = request.form['images']
        price = request.form['price']
        desc = request.form['desc']
        stock = request.form['stock']
        db_item = ProductModels(
            title=title,
            images=images,
            price=price,
            desc=desc,
            stock=stock,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return redirect(url_for('admin_dashboard_all_product'))

    return "<p>Here form to login</p>"


@app.route("/dashboard/edit-product/<int:product_id>")
def admin_dashboard_edit_product(product_id):
    if session['user'] != 'admin':
        return redirect(url_for('admin_login_form'))
    
    db_item = db.query(ProductModels).filter(ProductModels.id == product_id).first()
    if db_item is None:
        raise "<p>Error Product Not Found</p>"
    
    if request.method == "POST":
        db_item.title = request.form['title']
        db_item.images = request.form['images']
        db_item.price = request.form['price']
        db_item.desc = request.form['desc']
        db_item.stock = request.form['stock']
        db_item.updateAt = time.time()
        db.commit()
        db.refresh(db_item)
        return redirect(url_for('admin_dashboard_all_product'))

    return "<p>Here form to Edit Product</p>"


@app.route("/dashboard/delete-product/<int:product_id>")
def admin_dashboard_delete_product(product_id):
    return "<p>Here form to login</p>"

# ===============================================


# CART ROUTES ====================================

@app.route("/keranjang")
def 

# ================================================