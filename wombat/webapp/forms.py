from wombat.engine import ml_model
from wombat.models import engine, dbsession, Item
from wtforms import Form, StringField, SubmitField, SelectField, FloatField, validators

item_types = engine.execute('SELECT DISTINCT item_type,\
        count(item_type) FROM items GROUP BY item_type ORDER BY \
        count(item_type) DESC;').fetchall()
item_types = [(r[0], r[0].title()) for r in item_types]
brands_query = "SELECT * FROM brands;"
brands = ml_model.brands[0:100]
brand_names = sorted([b[1] for b in engine.execute(brands_query).fetchall()], key=str.lower)
brand_names.remove('other brand')
brands = [(b, b) for b in brand_names]
brands = [('', 'Choose a brand')] + [('other brand', 'Other')] + brands

class DescriptionForm(Form):
    description = StringField('Description')
    item_type = SelectField(label='Category', choices=item_types,
            validators=[validators.Required(message='Category is required')])
    brand = SelectField(label='Brand', choices=brands,
            validators=[validators.Required(message='Please choose a brand')])
    est_price = FloatField(label='Retail Price', validators =
    [validators.Required(message="""Please enter a retail price. If you
                don\'t know the exact price of the item you can estimate
                it or look for similar priced items""")])
    submit = SubmitField(label='Submit')

