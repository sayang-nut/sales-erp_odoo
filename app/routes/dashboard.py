from flask import Blueprint, render_template
from flask_login import login_required
from app.models.order import Order
from app.models.product import Product
from app.models.customer import Customer

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    stats = {
        'total_orders': Order.query.count(),
        'total_products': Product.query.count(),
        'total_customers': Customer.query.count(),
        'recent_orders': Order.query.order_by(Order.created_at.desc()).limit(5).all()
    }
    return render_template('dashboard/index.html', stats=stats)
