from flask import Flask , render_template,request, redirect,url_for,flash,session
from database import get_products, get_stock, get_sales,insert_products,insert_sales,insert_stock,available_stock,check_user_exists,insert_user,get_sales_per_day,get_profit_per_day,get_profit_per_product,get_sales_per_product
from flask_bcrypt import Bcrypt
from functools import wraps


# flask instance
app = Flask(__name__)

# bcrypt instance
bcrypt = Bcrypt(app)


app.secret_key = 'obsta.cal'



# home route
@app.route('/')
def index():
    return render_template('index.html')



def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


# products route
@app.route('/products')
def products():
    products= get_products()
    return render_template('products.html',products = products)


@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST': 
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']

        new_product = ( product_name, buying_price, selling_price )
        insert_products(new_product)
        flash("Product added successfully",'success')
    return redirect(url_for('products'))



# sales route
@app.route('/sales')
def sales():
    sales= get_sales()
    products = get_products()
    return render_template('sales.html',sales = sales,products = products)


@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']
        
        new_sale = (pid, quantity)
        check_stock = available_stock(pid)
        if check_stock < float(quantity):
            flash(f"Insufficient stock to complete sale, only {check_stock} available", 'danger')
            return redirect(url_for('sales'))
        
        insert_sales(new_sale)
        flash("Sale made successfully", 'success')
    
    return redirect(url_for('sales'))



# stock route
@app.route('/stock')
def stock():
    stock = get_stock()
    products = get_products()
    return render_template('stock.html', stock=stock, products=products)


@app.route('/add_stock',methods=['GET','POST'])
def count_stock():
    if request.method == 'POST':
        pid = request.form['pid']
        stock_quantity = request.form['s_quantity']
        
        new_stock = (pid, stock_quantity)
        insert_stock(new_stock)
        
        flash("Stock made successfully", 'success')
        
    return redirect(url_for('stock'))



# dashboard route
@app.route('/dashboard')
def dashboard():
    sales_per_product = get_sales_per_product()
    profit_per_product = get_profit_per_product()

    sales_per_day = get_sales_per_day()
    profit_per_day = get_profit_per_day()

    product_names = [i[0] for i in sales_per_product]
    product_sales = [ float (i[1]) for i in sales_per_product]
    product_profit = [ float (i[1]) for i in profit_per_product]

    dates = [ str (i[0]) for i in sales_per_day]
    daily_sales = [ float (i[1]) for i in sales_per_day]
    daily_profit = [ float (i[1]) for i in profit_per_day]
    
    return render_template('dashboard.html',product_names = product_names, product_sales = product_sales, product_profit = product_profit, dates = dates, daily_sales = daily_sales, daily_profit = daily_profit)



# login route
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        existing_user = check_user_exists(email)
        if not existing_user:
            flash("User with this email not registered", 'danger')
            return redirect(url_for('login'))
        
        check_password = bcrypt.check_password_hash(existing_user[-1],password)
        
        if check_password:
            session['email'] = email
            flash("Login successful", 'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Incorrect password,try again", 'danger')
            return redirect(url_for('login'))
        
    return render_template('login.html')



# register route
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = check_user_exists(email)
        if existing_user:
            flash("User with this email already exists, Login instead","danger")
            return (redirect(url_for('register')))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = (full_name,email,phone_number,hashed_password)
        insert_user(new_user)
        flash("User created successfully",'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("Logged out successfully",'success')
    return redirect(url_for('login'))


app.run(debug=True)