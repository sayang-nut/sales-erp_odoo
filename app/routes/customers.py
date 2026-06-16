from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from app import db
from app.models.customer import Customer

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

def admin_required():
    if current_user.role != 'admin':
        flash('Bạn cần quyền admin để thực hiện thao tác này.', 'danger')
        return redirect(url_for('dashboard.index'))
    return None

@customers_bp.route('/')
@login_required
def index():
    customers = Customer.query.all()
    return render_template('customer/index.html', customers=customers)

@customers_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if result := admin_required():
        return result

    if request.method == 'POST':
        customer = Customer(
            name=request.form['name'],
            email=request.form.get('email') or None,
            phone=request.form.get('phone') or None,
            address=request.form.get('address') or None
        )
        db.session.add(customer)
        db.session.commit()
        flash('Thêm khách hàng thành công!', 'success')
        return redirect(url_for('customers.index'))
    return render_template('customer/create.html')

@customers_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    if result := admin_required():
        return result

    customer = Customer.query.get_or_404(id)
    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form.get('email') or None
        customer.phone = request.form.get('phone') or None
        customer.address = request.form.get('address') or None
        db.session.commit()
        flash('Cập nhật khách hàng thành công!', 'success')
        return redirect(url_for('customers.index'))
    return render_template('customer/edit.html', customer=customer)

@customers_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    if result := admin_required():
        return result

    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    flash('Đã xóa khách hàng!', 'success')
    return redirect(url_for('customers.index'))
