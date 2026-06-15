from app import create_app, db
from app.models.product import Product, Category
from app.models.customer import Customer

app = create_app()

with app.app_context():
    # Tránh tạo trùng nếu đã có data
    if Category.query.count() > 0:
        print("⚠️  Đã có dữ liệu, bỏ qua seed.")
        exit()

    # --- Categories ---
    cat_electronics = Category(name='Điện tử')
    cat_office = Category(name='Văn phòng phẩm')
    cat_food = Category(name='Thực phẩm')
    db.session.add_all([cat_electronics, cat_office, cat_food])
    db.session.flush()  # để lấy id của category

    # --- Products ---
    products = [
        Product(name='Chuột không dây Logitech', sku='ELEC-001', price=250000, stock=50, category_id=cat_electronics.id),
        Product(name='Bàn phím cơ AKKO', sku='ELEC-002', price=890000, stock=20, category_id=cat_electronics.id),
        Product(name='Tai nghe Sony WH-1000', sku='ELEC-003', price=4500000, stock=10, category_id=cat_electronics.id),
        Product(name='Bút bi Thiên Long', sku='OFF-001', price=5000, stock=500, category_id=cat_office.id),
        Product(name='Sổ tay A5', sku='OFF-002', price=25000, stock=200, category_id=cat_office.id),
        Product(name='Giấy in A4 Double A', sku='OFF-003', price=65000, stock=100, category_id=cat_office.id),
        Product(name='Cà phê hòa tan G7', sku='FOOD-001', price=85000, stock=80, category_id=cat_food.id),
        Product(name='Trà xanh Lipton', sku='FOOD-002', price=45000, stock=60, category_id=cat_food.id),
    ]
    db.session.add_all(products)

    # --- Customers ---
    customers = [
        Customer(name='Công ty TNHH ABC', email='abc@company.com', phone='0901234567', address='123 Nguyễn Huệ, Q1, TP.HCM'),
        Customer(name='Nguyễn Văn An', email='an.nguyen@gmail.com', phone='0912345678', address='45 Lê Lợi, Q.Bình Thạnh, TP.HCM'),
        Customer(name='Công ty Cổ phần XYZ', email='contact@xyz.vn', phone='0923456789', address='78 Trần Hưng Đạo, Q5, TP.HCM'),
        Customer(name='Trần Thị Bình', email='binh.tran@gmail.com', phone='0934567890', address='90 Cách Mạng Tháng 8, Q.Tân Bình, TP.HCM'),
    ]
    db.session.add_all(customers)

    db.session.commit()
    print("✅ Seed data thành công!")
    print(f"   - {Category.query.count()} categories")
    print(f"   - {Product.query.count()} products")
    print(f"   - {Customer.query.count()} customers")
