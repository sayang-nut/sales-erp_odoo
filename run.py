from app import create_app, db
from sqlalchemy import inspect, text

app = create_app()

with app.app_context():
    from app.models.user import User
    from app.models.product import Product, Category
    from app.models.customer import Customer
    from app.models.order import Order, OrderLine

    db.create_all()

    inspector = inspect(db.engine)
    with db.engine.begin() as conn:
        if inspector.has_table('orders'):
            order_columns = {col['name'] for col in inspector.get_columns('orders')}
            if 'created_by' not in order_columns:
                conn.execute(text("ALTER TABLE orders ADD COLUMN IF NOT EXISTS created_by INTEGER REFERENCES users(id);"))
                print('Added orders.created_by column')
        if inspector.has_table('products'):
            product_columns = {col['name'] for col in inspector.get_columns('products')}
            if 'created_by' not in product_columns:
                conn.execute(text("ALTER TABLE products ADD COLUMN IF NOT EXISTS created_by INTEGER REFERENCES users(id);"))
                print('Added products.created_by column')

    print("Tables created or updated successfully!")

if __name__ == '__main__':
    app.run(debug=True)
