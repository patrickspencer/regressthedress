from wombat.engine import ml_model
from wombat.models import engine, dbsession, Item
from wtforms import Form, StringField, SubmitField, SelectField, validators

item_types = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
item_types = [(r[0], r[0]) for r in item_types]
brands_query = "SELECT * FROM brands;"
brands = ml_model.brands[0:100]
brand_names = sorted([b[1] for b in engine.execute(brands_query).fetchall()], key=str.lower)
brand_names.remove('other brand')
brands = [(b, b) for b in brand_names]
brands = [('', 'Choose a brand')] + [('other brand', 'Other')] + brands

class DescriptionForm(Form):
    description = StringField('Description', [validators.Length(min=1, max=5000)])
    submit = SubmitField(label='Submit')
    item_type = SelectField(label='Category', choices=item_types)
    brand = SelectField(label='Brand', choices=brands, validators=[validators.Required(message='Brand is required')])
    est_price = StringField(label='Price')

