from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import admin
from .forms import ProductForm,RoleForm,UserAssignForm, SupplyVerdict, PayStatus
from .. import db
from ..models import Product,Role,User,SupplyRequest

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Product Views


@admin.route('/', methods=['GET', 'POST'])
@login_required
def list_products():
    """
    List all products
    """
    check_admin()

    products = Product.query.all()

    return render_template('home/products/product.html',
                           products=products, title="Products")

@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the role page
        return redirect(url_for('admin.list_roles'))

    # load role template 
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')

@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")

@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    
    return render_template('admin/users/users.html',
                           users=users, title='Users')

@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a role to an user
    """
    check_admin()

    user = User.query.get_or_404(id)
    print(user)
    # prevent admin from being assigned  a role
    if user.is_admin:
        abort(403)

    form = UserAssignForm(obj=user)
    if form.validate_on_submit():
        user.role = form.role.data
        db.session.add(user)
        db.session.commit()
        

        # redirect to the roles page
        return redirect(url_for('admin.list_users'))

    return render_template('admin/users/user.html',user=user, form=form,title='Assign User')


@admin.route('/users/request/<int:id>', methods=['GET', 'POST'])
@login_required
def check_requests(id):
    """
    Assign a role to an user
    """
    check_admin()

    request = SupplyRequest.query.get_or_404(id)

    form = SupplyVerdict()
    if form.validate_on_submit():
        request.approval_status = form.status.data
        db.session.add(request)
        db.session.commit()

        # redirect to the roles page
        return redirect(url_for('home.admin_dashboard'))

    return render_template('home/approve.html',request=request, form=form,title='Approve Requests')


@admin.route('/users/payment/<int:id>', methods=['GET', 'POST'])
@login_required
def check_payment(id):
    """
    Assign a role to an user
    """
    check_admin()

    product = Product.query.get_or_404(id)

    form = PayStatus()
    if form.validate_on_submit():
        product.status = form.status.data
        db.session.add(product)
        db.session.commit()

        # redirect to the roles page
        return redirect(url_for('home.admin_dashboard'))

    return render_template('home/paid.html',product=product, form=form,title='Payment Status')