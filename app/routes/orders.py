from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models.order import Order, OrderLine
from app.models.product import Product
from app.models.customer import Customer
import uuid

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

def generate_order_code():
    return 'ORD-' + str(uuid.uuid4())[:8].upper()

@orders_bp.route('/')
@login_required
def index():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('orders/index.html', orders=orders)

@orders_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    customers = Customer.query.all()
    products = Product.query.filter_by(is_active=True).all()
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        product_ids = request.form.getlist('product_id')
        quantities = request.form.getlist('quantity')

        order = Order(
            order_code=generate_order_code(),
            customer_id=customer_id,
            status='draft'
        )
        db.session.add(order)
        db.session.flush()  # lấy order.id trước khi commit

        total = 0
        for pid, qty in zip(product_ids, quantities):
            product = Product.query.get(pid)
            qty = int(qty)
            subtotal = product.price * qty
            total += subtotal
            line = OrderLine(
                order_id=order.id,
                product_id=pid,
                quantity=qty,
                unit_price=product.price,
                subtotal=subtotal
            )
            db.session.add(line)

        order.total_amount = total
        db.session.commit()
        flash(f'Tạo đơn hàng {order.order_code} thành công!', 'success')
        return redirect(url_for('orders.index'))

    return render_template('orders/create.html', customers=customers, products=products)

@orders_bp.route('/<int:id>/status', methods=['POST'])
@login_required
def update_status(id):
    order = Order.query.get_or_404(id)
    new_status = request.form['status']
    order.status = new_status
    db.session.commit()
    flash('Cập nhật trạng thái thành công!', 'success')
    return redirect(url_for('orders.index'))
