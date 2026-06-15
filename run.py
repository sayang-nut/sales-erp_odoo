from app import create_app, db

app = create_app()

with app.app_context():
    from app.models.user import User
    from app.models.product import Product, Category
    from app.models.customer import Customer
    from app.models.order import Order, OrderLine
    
    db.create_all()
    print(" Tables created successfully!")

if __name__ == '__main__':
    app.run(debug=True)