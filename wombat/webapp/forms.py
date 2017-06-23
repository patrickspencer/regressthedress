from wombat.engine import ml_model
from wombat.models import engine, dbsession, Item
from wtforms import Form, StringField, SubmitField, SelectField, validators

item_types = engine.execute('SELECT DISTINCT item_type FROM items;').fetchall()
item_types = [(r[0], r[0]) for r in item_types]
# brands = engine.execute('SELECT DISTINCT brand, COUNT(brand) FROM items WHERE brand != 'LENDER SUBMISSION FILL IN' GROUP BY brand ORDER BY count(brand) DESC LIMIT 30;').fetchall()
brands = ml_model.brands[0:100]
brands = [(b, b) for b in brands]


class DescriptionForm(Form):
    description = StringField('Description', [validators.Length(min=1, max=5000)])
    submit = SubmitField(label='Submit')
    item_type = SelectField(label='Category', choices=item_types)
    brand = SelectField(label='Brand', choices=brands)
    est_price = StringField(label='Price Range')

