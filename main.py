from flask import Flask , render_template,request, redirect,url_for,flash
from database import get_products, get_stock, get_sales,insert_products,insert_sales,insert_stock

# flask instance
app = Flask(__name__)

app.secret_key = 'obsta.cal'


# home route
@app.route('/')
def index():
    return render_template('index.html')


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
    return render_template('dashboard.html')

# login route
@app.route('/login')
def login():
    return render_template('login.html')

# register route
@app.route('/register')
def register():
    return render_template('register.html')


app.run(debug=True)