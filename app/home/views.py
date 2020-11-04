#Views for home page
from flask import render_template,flash, request, redirect, url_for
from flask_login import login_user, logout_user,login_required, current_user
from app.models import User, SupplyRequest, Product
from .. import db
from .forms import SupplyRequestForm, ProductForm

from . import home
# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        
        return redirect(url_for("home.dataentry"))
    products = Product.query.all()
    request = SupplyRequest.query.all()
    items = Product.query.count()
    users = User.query.count()
    return render_template('home/dashboard.html', title="Dashboard", products=products,request=request, items = items,users=users)

@home.route('/')
def landingpage():
    """
    Render the landing home page template on the / route
    """
    return render_template('home/index.html', title="Welcome to the home page")

@home.route('/dashboard')
@login_required
def dataentry():
    """
    Render the dashboard page template on the /dashboard route
    """
    products = Product.query.all()
    request = SupplyRequest.query.all()
    items = Product.query.count()
    return render_template('home/dataentry.html', title="Welcome to the dashboard", products=products, request=request, items=items)    

@home.route('/request',methods = ["POST","GET"])
@login_required
def request():
    
    form = SupplyRequestForm()
    if form.validate_on_submit():
        productname = form.productname.data
        total_required = form.total_required.data

        new_request = SupplyRequest(productname=productname,total_required=total_required,user_id=current_user.id)
        db.session.add(new_request)
        db.session.commit()
        return redirect(url_for("home.dataentry"))

    return render_template('home/request.html', title="Create your request:", form=form)    

@home.route('/request/<int:request_id>/delete')
@login_required
def delete_request(request_id):
    
    request = SupplyRequest.query.filter_by(id=request_id).first_or_404()
    db.session.delete(request)
    db.session.commit()
    
    return redirect(url_for("home.dataentry"))

@home.route('/add',methods = ["POST","GET"])
@login_required
def add_product():

    form = ProductForm()
    if form.validate_on_submit():
        productname = form.productname.data
        productspoilt = form.productspoilt.data
        quantity = form.quantity.data
        stock = form.stock.data
        totalprice = form.totalprice.data
        status = form.status.data

        new_product = Product(productname=productname,productspoilt=productspoilt,quantity=quantity,stock=stock,status=status,totalprice=totalprice)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for("home.dataentry"))

    return render_template('home/products/products.html', title="Add Product", form=form)