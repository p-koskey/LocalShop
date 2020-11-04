from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,RadioField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import SupplyRequest,Product

class ProductForm(FlaskForm):
    """
    """
    productname = StringField('Enter Your  Product Name:', validators=[DataRequired()])
    productspoilt = IntegerField('Number spoilt:')
    quantity = IntegerField('Number of product Received:')
    stock = IntegerField('Number of product in stock:')
    totalprice = IntegerField('Total price :')
    status = RadioField('Label', choices = [('paid', 'paid'),('unpaid', 'unpaid')], validators = [DataRequired()])
    submit  = SubmitField('Submit')

class SupplyRequestForm(FlaskForm):
    """
    Form for data clerk to request for product supply
    """
    productname = StringField('Product Name:', validators=[DataRequired()])
    total_required = IntegerField('Total Required:',validators=[DataRequired()])
    submit = SubmitField('Submit')