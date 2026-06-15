from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models.product import Product, Category

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
@login_required
def index():
    products = Product.query.filter_by(is_active=True).all()
    return render_template('products/index.html', products=products)

@products_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    categories = Category.query.all()
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            sku=request.form['sku'],
            price=request.form['price'],
            stock=request.form['stock'],
            category_id=request.form.get('category_id') or None
        )
        db.session.add(product)
        db.session.commit()
        flash('Thêm sản phẩm thành công!', 'success')
        return redirect(url_for('products.index'))
    return render_template('products/create.html', categories=categories)

@products_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    product = Product.query.get_or_404(id)
    categories = Category.query.all()
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.stock = request.form['stock']
        product.category_id = request.form.get('category_id') or None
        db.session.commit()
        flash('Cập nhật thành công!', 'success')
        return redirect(url_for('products.index'))
    return render_template('products/edit.html', product=product, categories=categories)

@products_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    product = Product.query.get_or_404(id)
    product.is_active = False
    db.session.commit()
    flash('Đã xóa sản phẩm!', 'success')
    return redirect(url_for('products.index'))
