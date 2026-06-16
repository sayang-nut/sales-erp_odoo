# 🏢 Mini ERP Sales

Một ứng dụng quản lý bán hàng mini được xây dựng với Flask. Cung cấp các tính năng quản lý sản phẩm, khách hàng, đơn hàng và xác thực người dùng.

## ✨ Tính năng chính

- 👤 **Quản lý người dùng**: Đăng ký, đăng nhập, phân quyền admin
- 📦 **Quản lý sản phẩm**: Thêm, sửa, xóa sản phẩm; Quản lý danh mục
- 👥 **Quản lý khách hàng**: Thêm, sửa, xóa khách hàng; Lưu thông tin liên hệ
- 🛒 **Quản lý đơn hàng**: Tạo đơn hàng, theo dõi trạng thái, quản lý chi tiết đơn hàng
- 📊 **Dashboard**: Tổng quan về hệ thống

## 🛠️ Yêu cầu hệ thống

- Python 3.8 trở lên
- PostgreSQL (hoặc SQLite cho phát triển)
- pip (Python package manager)

## 📋 Cài đặt

### 1. Clone dự án

```bash
git clone <repository-url>
cd sales-erp
```

### 2. Tạo môi trường ảo

```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Cấu hình biến môi trường

Tạo file `.env` trong thư mục gốc:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://username:password@localhost:5432/sales_erp
# Hoặc dùng SQLite: sqlite:///sales_erp.db
```

### 5. Khởi tạo Database

```bash
python run.py
```

Hoặc sử dụng seed data:

```bash
python seed_data.py
```

## 🚀 Chạy ứng dụng

```bash
python run.py
```

Ứng dụng sẽ chạy tại: `http://localhost:5000`

## 📁 Cấu trúc dự án

```
sales-erp/
├── app/
│   ├── __init__.py           # Khởi tạo Flask app
│   ├── models/
│   │   ├── user.py          # Model người dùng
│   │   ├── product.py       # Model sản phẩm & danh mục
│   │   ├── customer.py      # Model khách hàng
│   │   └── order.py         # Model đơn hàng
│   ├── routes/
│   │   ├── auth.py          # Routes xác thực
│   │   ├── dashboard.py     # Routes dashboard
│   │   ├── products.py      # Routes sản phẩm
│   │   ├── customers.py     # Routes khách hàng
│   │   └── orders.py        # Routes đơn hàng
│   ├── templates/
│   │   ├── base.html        # Template cơ sở
│   │   ├── auth/            # Templates xác thực
│   │   ├── dashboard/       # Templates dashboard
│   │   ├── products/        # Templates sản phẩm
│   │   ├── customer/        # Templates khách hàng
│   │   └── orders/          # Templates đơn hàng
│   └── static/
│       ├── css/             # Stylesheets
│       └── js/              # JavaScript
├── run.py                    # File chạy ứng dụng
├── seed_data.py             # Dữ liệu mẫu
├── requirements.txt         # Dependencies
└── README.md                # Tài liệu này
```

## 🔐 Hệ thống xác thực

- **Đăng ký tài khoản**: Tạo tài khoản người dùng mới
- **Đăng nhập**: Xác thực người dùng với username/password
- **Phân quyền**: 
  - Admin: Có quyền quản lý sản phẩm, khách hàng, đơn hàng
  - User: Có quyền xem dashboard và danh sách

## 📦 Quản lý sản phẩm

- Thêm sản phẩm với SKU, tên, giá, tồn kho
- Phân loại sản phẩm theo danh mục
- Sửa thông tin sản phẩm
- Xóa sản phẩm (soft delete)

## 👥 Quản lý khách hàng

- Thêm khách hàng với thông tin: tên, email, điện thoại, địa chỉ
- Xem danh sách khách hàng
- Cập nhật thông tin khách hàng
- Xóa khách hàng

## 🛒 Quản lý đơn hàng

- Tạo đơn hàng mới
- Thêm sản phẩm vào đơn hàng (OrderLine)
- Cập nhật trạng thái đơn hàng (Draft, Confirmed, Shipped, Done, Cancelled)
- Tính tổng tiền tự động
- Xem chi tiết đơn hàng

## 🗄️ Models (Database Schema)

### User
- id, username, email, password_hash, role, created_at

### Product
- id, name, sku, price, stock, category_id, is_active, created_by, created_at

### Category
- id, name, description

### Customer
- id, name, email, phone, address, created_at

### Order
- id, order_code, customer_id, total_amount, status, created_by, created_at

### OrderLine
- id, order_id, product_id, quantity, unit_price, line_total

## 🎨 Frontend

- **Framework**: Bootstrap 5
- **Icons**: Bootstrap Icons
- **Template Engine**: Jinja2
- **Responsive Design**: Mobile-friendly UI

## 📝 API Endpoints

### Authentication
- `POST /login` - Đăng nhập
- `POST /register` - Đăng ký
- `GET /logout` - Đăng xuất

### Products
- `GET /products/` - Danh sách sản phẩm
- `GET /products/create` - Form thêm sản phẩm
- `POST /products/create` - Tạo sản phẩm
- `GET /products/<id>/edit` - Form sửa sản phẩm
- `POST /products/<id>/edit` - Cập nhật sản phẩm
- `POST /products/<id>/delete` - Xóa sản phẩm

### Customers
- `GET /customers/` - Danh sách khách hàng
- `GET /customers/create` - Form thêm khách hàng
- `POST /customers/create` - Tạo khách hàng
- `GET /customers/<id>/edit` - Form sửa khách hàng
- `POST /customers/<id>/edit` - Cập nhật khách hàng
- `POST /customers/<id>/delete` - Xóa khách hàng

### Orders
- `GET /orders/` - Danh sách đơn hàng
- `GET /orders/create` - Form tạo đơn hàng
- `POST /orders/create` - Tạo đơn hàng
- `POST /orders/<id>/update-status` - Cập nhật trạng thái đơn hàng

### Dashboard
- `GET /` - Dashboard chính

## 🧪 Development

### Chạy với reload tự động

```bash
flask run --reload
```

### Tạo dữ liệu mẫu

```bash
python seed_data.py
```

## 📦 Dependencies chính

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
Flask-Login==0.6.0
SQLAlchemy==2.0.0
python-dotenv==1.0.0
```

## 🔒 Bảo mật

- Mật khẩu được mã hóa bằng werkzeug
- Session-based authentication với Flask-Login
- CSRF protection
- Form validation
- SQL Injection protection thông qua SQLAlchemy ORM

## 📄 License

MIT License

## 👨‍💻 Author

Tạo bởi TuongDev

---

**Phiên bản**: 1.0.0  
**Cập nhật lần cuối**: 2026-06-16
